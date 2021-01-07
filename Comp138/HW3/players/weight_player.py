import numpy as np
import random
from players.player import Player


class TileWeightPlayer(Player):
    """
    A baseline player that evaluates a state by assigning different weights to
    different tiles and summing up the result
    """

    def __init__(self, weights, seed=None):
        super().__init__(len(weights), 0, seed)
        self._weights = np.array(weights)
        assert(len(weights) == len(weights[0]))

    def act_from_state(self, board):
        """
        Returns an afterstate that maximizes the rewards
        :param board: a reversi board
        :return:
        """
        afterstates = board.afterstates()
        rewards = [-np.sum(a._board * self._weights) for a in afterstates]
        max_reward = max(rewards)

        # Break ties randomly so we could explore all the states
        index = [i for i in range(len(afterstates)) if rewards[i] == max_reward]
        return afterstates[random.choice(index)]

    def act(self, states):
        """
        Maps act_from_state onto states
        :param states:
        :return:
        """
        return [self.act_from_state(state) for state in states]

    def train(self, history):
        """ TileWeightPlayer requires no training """
        pass
