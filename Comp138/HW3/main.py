from reversi import ReversiState
from players.weight_player import TileWeightPlayer
from players.rl_player import RLPlayer
from tqdm import tqdm
import numpy as np


def play_batch(starting_state, players, n_games):
    """
    Play n_games simultaneously
    :param starting_state:   The starting state for all games
    :param players:          Players[0] always makes the first move
    :param n_games:          Number of games to play
    :return:                 (history, results), where
                              - history is the 2d array such that
                                history[i][j] is the ReversiState after i moves
                                in the jth game if terminal state has not been
                                reached yet, or None otherwise.
                              - results - a 2d array that for each game and each
                                player records the scores each player received
                                in the game
    """
    max_moves = 2 * starting_state.get_size() ** 2
    curr = np.full(shape=(max_moves, n_games), fill_value=None, dtype=object)
    history = np.copy(curr)  # finished games
    curr[0, ] = starting_state
    results = np.zeros(shape=(n_games, 2), dtype=np.int)
    for move in range(max_moves - 1):
        curr[move + 1, :] = players[move % 2].act(curr[move])
        if move == 0:
            continue
        game = 0
        while game < curr.shape[1]:
            if curr[move + 1][game] != curr[move - 1][game]:
                game += 1
                continue
            score = curr[move - 1][game].get_score()
            results[curr.shape[1]-1] = [score[(move - 1) % 2], score[move % 2]]
            history[:move + 1, n_games - curr.shape[1]] = curr[:move + 1, game]
            curr = np.delete(curr, game, 1)
        if curr.shape[1] == 0:
            break
    return history, results


def play(starting_state, players, n_games, batch_size, train=True,
         keep_results=False):
    """
    Play n_games games between two players. Play batch_size games
    simultaneously. Alternate the first player ot move between batches
    :param starting_state:  the state from which to start each game
    :param players:         a tuple of two reversi players
    :param n_games:         total number of games to play
    :param batch_size:      number of games to play simultaneously
    :param train:           whether to train the players after each batch.
    :param keep_results:    whether to preserve the scores for each game
    :return:
    """
    assert (n_games % batch_size == 0)
    assert ((n_games // batch_size) % 2 == 0)
    if keep_results:
        results = np.zeros(shape=(n_games, 2), dtype=np.int)
    bar = tqdm(range(n_games // batch_size))  # progressbar
    turn = (0, 1)
    for batch in bar:
        history, curr_results = play_batch(starting_state,
                                           (players[turn[0]],
                                            players[turn[1]]),
                                           batch_size)
        if keep_results:
            results[batch * batch_size: (batch + 1) * batch_size] = \
                curr_results[:, turn]
        if train:
            players[turn[0]].train(history[1:, ])
            players[turn[1]].train(history[2:, ])
        bar.set_description("Batch. WinRate: %s" %
                            (str(round(np.mean(curr_results[:, turn[0]] >
                                              curr_results[:, turn[1]]), 3))))
        turn = (turn[1], turn[0])  # change who goes first
    if keep_results:
        return np.array(results)


def compare(players, descs, starting_state, n_games=300, batch_size=50):
    """
    Pits each of the players in players against each other player and
    reports the winning rate in each case.
    :param players:  List of players to pit against each other
    :param descs:    String names of the players
    :param n_games:  Number of games to play for each pair
    :param batch_size:     Batch-size to use in each case
    :param starting_state: The state with which ti start each game
    :return: None
    """
    for player in players:
        player.exploration_on = False
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            results = play(starting_state=starting_state,
                           players=(players[i], players[j]), n_games=n_games,
                           batch_size=batch_size, train=False,
                           keep_results=True)
            win_rate = np.sum(results[:, 0] > results[:, 1]) / len(results)
            print("%s player beats the %s player in %f of the games" %
                  (descs[i], descs[j], win_rate))
    for player in players:
        player.exploration_on = True


if __name__ == "__main__":
    twp = TileWeightPlayer([[100, -25, 10, 10, -25, 100],
                            [-25,  -25,  5,  5, -25, -25],
                            [10,     5,  1,  1,   5,  10],
                            [10,     5,  1,  1,   5,  10],
                            [-25,  -25,  5,  5, -25, -25],
                            [100,  -25, 10, 10, -25, 100]], seed=0)
    randomp = TileWeightPlayer([[0] * 6] * 6, seed=1)

    rlp = RLPlayer(6, 0.01, seed=3)
    # """
    print("Training RL agent against the weight-based heuristic player "
          "for 20000 games...")
    play(starting_state=ReversiState(6), players=(rlp, twp), n_games=100000,
         batch_size=10)
    rlp.save("data/rlbase_moves")
    # """
    # rlp.load("data/rlbase")

    print("Comparing all the agents to each other:")
    compare([rlp, twp, randomp],
            ["RL", "RL (trained with transfer)",
             "weight-based", "move-based", "random"],
            starting_state=ReversiState(6))