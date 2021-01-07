import numpy as np
from cnn import ReversiCNN
from players.player import Player


class RLPlayer(Player):
    """
    Deep RL Player (currently implemented like Sarsa with CNN
    as a function approximator)
    """

    TD_N = 6  # this player uses the SARSA(TD_N) strategy

    def __init__(self, size, epsilon, seed=None):
        """
        Create a player for a certain board size
        :param size:    Size of the board for which to create an agent
        :param epsilon: Exploration rate
        :param seed:    Random seed to use
        """
        super().__init__(size, epsilon, seed)
        # self.approximators are unique approximation functions
        # (several functions for different levels)
        self.approximators = [ReversiCNN(size, [3], 3, [10])
                              for _ in range((size ** 2) + 1)]
        self.buffers = [Buffer(3000, size) for a in self.approximators]
        # level_to_approx marks the game progression level (# pieces on board)
        # to the approximation funcvtion that must be used
        self.level_to_approx = {i: self.approximators[i]
                                for i in range(size ** 2 + 1)}
        self.level_to_buffer = {i: self.buffers[i]
                                for i in range(size ** 2 + 1)}


    def act(self, states):
        """
        For each state in states choose an action (i.e. afterstate) to execute
        :param states:
        :return:
        """
        afterstates = [state.afterstates() for state in states]
        cnn_input_vector = np.array([item.numpy() for sublist in afterstates
                                     for item in sublist])
        # TODO: note that pieces on board might be different for different
        # TODO: states - not sure how to fix this without breaking batching.
        # TODO: also - stop running CNN on the same state several times
        estimates = self.level_to_approx[afterstates[0][0].pieces_on_board()].\
            evaluate(cnn_input_vector)
        result = []
        pos = 0  # position in estimates corresponding to current state analyzed
        for i in range(len(states)):
            if self.explore():  # explore
                action_id = self._generator.integers(0, len(afterstates[i]))
                result.append(afterstates[i][action_id])
                pos += len(afterstates[i])
                continue
            if i != len(afterstates) - 1:
                estimates_for_state = estimates[pos: pos + len(afterstates[i])]
            else:
                estimates_for_state = estimates[pos:]
            min = np.amin(estimates_for_state)
            argmin = np.argwhere(estimates_for_state == min).flatten()
            action_id = argmin[self._generator.integers(0, len(argmin))]
            result.append(afterstates[i][action_id])
            pos += len(afterstates[i])
        return result

    def train(self, history):
        """
        Train the agent on history.shape[1] previous games
        :param history:
        :return:
        """
        for i in range(0, len(history) - 2, 2):
            before = history[i]  # afterstates chosen by the player

            after = np.full(shape=len(history[i]), fill_value=None)
            for game in range(len(history[i])):
                for offset in range(20, 0, -2):
                    if history[i + offset][game] is not None:
                        after[game] = history[i + offset][game]
                        break

            # discard the states after the game already ended
            not_none = [i for i in range(len(after)) if after[i] is not None]
            if len(not_none) == 0:
                break
            after = after[not_none]
            before = before[not_none]

            # TODO: note that pieces on board might be different for different
            # TODO: states - not sure how to fix this without breaking batching
            level = before[0].pieces_on_board()

            terminal = [i for i in range(len(after)) if after[i].is_terminal()]
            terminal_scores = [state.get_score() for state in after[terminal]]
            terminal_scores = [x[0]>x[1] for x in terminal_scores]
            after[terminal] = terminal_scores

            non_terminal = [i for i in range(len(after)) if i not in terminal]
            to_estimate = np.array([x.numpy() for x in after[non_terminal]])
            if len(to_estimate) > 0:
                estimates = self.level_to_approx[level + 1].evaluate(to_estimate)
                after[non_terminal] = estimates

            before = [x.numpy() for x in before]
            after = np.array(after, dtype=np.float)

            # update buffer and train
            self.level_to_buffer[level].add(before, after)
            x, y = self.level_to_buffer[level].select(len(before) * 10)
            self.level_to_approx[level].train_on_batch(x, y)

    def save(self, dir):
        for i in range(len(self.approximators)):
            self.approximators[i].save(dir + "/" + str(i) + ".model")

    def load(self, dir):
        for i in range(len(self.approximators)):
            self.approximators[i].load(dir + "/" + str(i) + ".model")


class Buffer:
    """
    For buffering reversi states
    """

    def __init__(self, buffer_size, board_size):
        self.y = np.zeros(buffer_size)
        self.x = np.zeros(shape=(buffer_size, 2, board_size, board_size))
        self.buffer_total = 0
        self.next_in_buffer = 0

    def add(self, x, y):
        if len(x) + self.next_in_buffer > len(self.x):
            diff = len(x) + self.next_in_buffer - len(self.x)
            self.y[self.next_in_buffer:] = y[:-diff]
            self.y[0:diff] = y[-diff:]
            self.x[self.next_in_buffer:] = x[:-diff]
            self.x[0:diff] = x[-diff:]
            self.next_in_buffer = diff
        elif len(x) + self.next_in_buffer == len(self.x):
            self.y[self.next_in_buffer:] = y
            self.x[self.next_in_buffer:] = x
            self.next_in_buffer = 0
        else:
            self.y[self.next_in_buffer: self.next_in_buffer + len(y)] = y
            self.x[self.next_in_buffer: self.next_in_buffer + len(x)] = x
            self.next_in_buffer += len(x)
        self.buffer_total += len(x)

    def select(self, n):
        idx = np.random.randint(0, min(self.buffer_total, len(self.x)), n)
        return self.x[idx], self.y[idx]