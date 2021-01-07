from players.weight_player import TileWeightPlayer
from players.minmoves_player import MinMovesPlayer
from task import *
from curriculum import *
from tqdm import tqdm
import numpy as np
import scipy.stats as stats
from reversi import ReversiState
from pathlib import Path

TEST_N_GAMES = 500  # number of games to play when testing
# various kinds of tasks
TARGET = OpponentTask(opponents={6: TileWeightPlayer(6),
                                 8: TileWeightPlayer(8)},
                      name="target")
RANDOM = OpponentTask(opponents={6: TileWeightPlayer(6, [[0] * 6] * 6),
                                 8: TileWeightPlayer(8, [[0] * 8] * 8)},
                      name="random")
MOVE_BASED = OpponentTask(opponents={6: MinMovesPlayer(6, seed=2),
                                     8: MinMovesPlayer(6, seed=2)},
                          name="move-based")
OPPONENT_BASED = [SelfPlayTask(), RANDOM, MOVE_BASED]
START_BASED = [StartingPositionTask(2/3, 1), StartingPositionTask(1/3, 2),
               StartingPositionTask(0, 3)]
EXPLORATION_BASED = [ExplorationRateTask(0.01), ExplorationRateTask(0.1)]


def play(task, n_games, train=True, keep_results=False,
         seed=None, win_rate_cutoff=10, win_rate_frame=500):
    """
    Play n_games games between two players. For each game, randomly decide
    who goes first
    :param task             a task to train on
    :param n_games:         total number of games to play
    :param train:           whether to train the players after each batch.
    :param keep_results:    whether to preserve the scores for each game
    :param seed:            random seed to use to decide who plays first in
                            each game
    :param win_rate_cutoff: the cutoff at which to stop training
    :param win_rate_frame:  frame for which to calculate the winning rate
    :return:
    """
    results = []
    generator = np.random.default_rng(seed)
    bar = tqdm(range(n_games))
    for i in bar:
        players, starting_state = task.get_new_game()
        init_turn = 0 if generator.random() > 0.5 else 1
        turn = init_turn
        history = [starting_state]
        while (len(history) < 3) or (history[-1] != history[-3]):
            next_state = players[turn].act(history[-1])
            history.append(next_state)
            turn = (turn + 1) % 2
        score = history[-1].get_score()

        results.append([score[turn], score[(turn + 1) % 2]])
        if not keep_results:
            results = results[-win_rate_frame:]

        if train:
            history = np.array(history[:-1])
            players[init_turn].train(history[1:, ])
            players[(init_turn + 1) % 2].train(history[2:, ])

        if i != 0 and i % win_rate_frame == 0:
            frame = min(len(results), win_rate_frame)
            win_rate = sum([x[0] > x[1] for x in results[-frame:]])/frame
            bar.set_description("Win_rate: " + str(win_rate))
            if win_rate > win_rate_cutoff:
                break

    if not keep_results:
        return []
    return np.array(results)


def try_to_load(filename):
    try:
        with open(filename) as file:
            return file.readlines()
    except:
        return None


def train_test_save(params, task, size, n_games, dir, agent=None,
                    test_task=None, seed=0):
    """
    Train an agent on a given task for a given number of games on a given board
    size, then set exploration to False and test the agent on the given task.
    Record training history and the final winning rate in the given directory.
    If the agent with given parameters was already trained, retreive and
    return the result
    :param params:  the parameters with which to initialize the agent
    :param task:    the task to train\test on
    :param size:    size of the board
    :param n_games: number of games to train for
    :param dir:     directory to save the data to
    :param test_task: task on which to test. If none, use the first task
    :param agent:   if not None, use the given agent instead of creating new one
    :param seed:    random seed to use. For testing, use seed + 1
    :return:        the test winning rate
    """
    params = deepcopy(params)
    key_string = "|".join([key + ":" + str(params[key])
                           for key in sorted(params.keys())])
    full_dir = dir + "/" + str(size) + "/" + key_string
    loaded = try_to_load(full_dir + "/stats.txt")
    if loaded:
        return float(loaded[0].strip("\n"))
    if not agent:
        agent = RLPlayer.from_params(size, seed, params)
    task.init(agent, ReversiState(size))
    train_result = play(task, n_games, train=True, keep_results=True, seed=seed)
    agent.set_exploration(False)
    if not test_task:
        test_task = task
    else:
        test_task.init(agent, ReversiState(size))
    test_results = play(test_task, TEST_N_GAMES, train=False, keep_results=True,
                        seed=seed + 1)
    win_rate = np.sum(test_results[:, 0] > test_results[:, 1]) / \
               len(test_results)
    Path(full_dir).mkdir(parents=True, exist_ok=True)
    with open(full_dir + "/stats.txt", "w") as file:
        results = [str(win_rate)] + [str(result[0]) + "\t" + str(result[1])
                                     for result in train_result]
        file.writelines("\n".join(results))
    agent.save(full_dir)
    agent.set_exploration(True)
    return win_rate


def hyperparameter_search(task, size, n_games, dir, params, set_params,
                          best_params=None, seed=0):
    """
    Perform greedy hyper-parameter search
    :param task:    the task on which to perform the search
    :param size:    the size of the board to perform the search for
    :param n_games: how long to continue training for
    :param dir:     the directory in which to store and record all the results
    :param params:  a list of parameters over which to perform the search
                    params[i][0] = parameter_name, params[i][1] - list of values
    :param set_params: parameters over which the search does not have to be
                       performed (as a dictionary)
    :param best_params: best parameters found so far
    :param seed:    random seed used by the agent and for training\testing loops
    :return:
    """
    if len(params) == 0:
        return train_test_save(set_params, task, size, n_games, dir, seed)
    new_set_params = deepcopy(set_params)
    for setting in params[1:]:
        new_set_params[setting[0]] = setting[1][0]
    best_result = 0
    param_name = params[0][0]
    print("Selecting best " + param_name)
    for param in params[0][1]:
        new_set_params[param_name] = param
        print("\tTrying " + str(param))
        new_result = hyperparameter_search(task, size, n_games, dir, [],
                                           new_set_params)
        print("\tGot " + str(new_result))
        if new_result >= best_result:
            best_params[param_name] = param
            best_result = new_result
    print("\tChoosing " + str(best_params[param_name]))
    set_params[param_name] = best_params[param_name]

    return hyperparameter_search(task, size, n_games, dir, params[1:],
                                 set_params, best_params)


def curriculum_tests(params, size, tasks, final_task, tasks_per_c,
                     games_per_task, n, dir, overwrite=False):
    """
    Conduct a slew of curriculum tests
    :param params: parameters with which to initialize every agent
    :param size:   size of the board to conduct the tests for
    :param tasks:  the tasks with which to generate the curricula
    :param final_task : task on which to train after all curricula
    :param tasks_per_c: tasks per curriculum
    :param games_per_task: number of games to play for each task
    :param n:      number of curricula to genenrate
    :param dir:    directory to save all the data to
    :param overwrite: if False, attempt to load a file with curricula
                      description before generating a new one
    :return:
    """
    meta_file = dir + "/meta_" + str(n) + "_" + str(tasks_per_c) + ".txt"
    try:
        curricula = Curriculum.load(meta_file, tasks)
    except:
        curricula = Curriculum.generate(tasks, n, tasks_per_c, final_task, 0)
        Curriculum.save(meta_file, curricula)

    win_rates = []

    for i, curriculum in enumerate(curricula):
        print("\n\nTraining an agent on curriculum # %d" % i)
        win_rate = curriculum.train(params, size, games_per_task,
                                    final_task, dir=dir + "/" + str(i),
                                    seed=i)
        print("Achieved win rate of %f" % win_rate)
        win_rates.append(win_rate)

    return win_rates


if __name__ == "__main__":

    # ------------ 6x6 BOARD ---------------------------------------------------

    # hyper-parameter search:
    best_params6 = {}
    hyperparameter_search(TARGET, 6, seed=0, n_games=20000,
                          dir="./results/hyper", best_params=best_params6,
                          params=[("n_approx", [1, 2, 4]),
                                  ("n", [20, 10, 2]),
                                  ("lr", [0.001, 0.01, 0.0001]),
                                  ("cnn_layers", [[3], [3, 6], [3, 6, 12]]),
                                  ("buffer_size", [3000, 1000]),
                                  ("epsilon", [0.01, 0.05])],
                          set_params={"buffer_update_size": 10, "kernel": 3,
                                      "ff_layers": [10]})
    best_params6["buffer_update_size"] = 10
    best_params6["kernel"] = 3
    best_params6["ff_layers"] = [10]
    # train for a long period of time:
    train_test_save(best_params6, TARGET, 6, 200000, dir="./results/long")

    # do curriculum learning experiments:
    tasks = [OPPONENT_BASED, EXPLORATION_BASED, START_BASED]
    final_task = TARGET.with_other_tasks([EXPLORATION_BASED[0]])
    rates6 = curriculum_tests(best_params6, 6, tasks=tasks,
                              final_task=final_task, tasks_per_c=2, n=10,
                              dir="./results/curriculum", overwrite=False,
                              games_per_task=10000)

    # ------------ 8x8 BOARD ---------------------------------------------------

    # hyper-parameter search:
    best_params8 = {}
    hyperparameter_search(TARGET, 8, seed=0, n_games=20000,
                          dir="./results/hyper", best_params=best_params8,
                          params=[("n_approx", [1, 2]),
                                  ("n", [20, 10, 2]),
                                  ("lr", [0.001, 0.01, 0.0001]),
                                  ("kernel", [3, 4]),
                                  ("buffer_size", [3000, 1000]),
                                  ("ff_layers", [[10], [50, 10]]),
                                  ("cnn_layers", [[3], [3, 6], [3, 6, 12]]),
                                  ("epsilon", [0.01, 0.05])],
                          set_params={"buffer_update_size": 10})
    best_params8["buffer_update_size"] = 10
    # train for a long period of time:
    train_test_save(best_params8, TARGET, 8, 200000, dir="./results/long")

    # do curriculum learning experiments:
    rates8 = curriculum_tests(best_params8, 8, tasks=tasks,
                              final_task=final_task, tasks_per_c=2, n=10,
                              dir="./results/curriculum", overwrite=False,
                              games_per_task=10000)

    print("Print Kendall's tau:" + str(stats.kendalltau(rates6, rates8)))
