import numpy as np


class Player:
    """ An abstract class to be extended by different Rerversi players"""

    def __init__(self, size, epsilon, seed=None):
        """
        Create a Reversi player for a certain board size
        :param size: size of the Reversi board
        :param epsilon: exploration rate
        """
        self._size = size
        self._epsilon = epsilon
        self._generator = np.random.default_rng(seed)
        self.exploration_on = True

    def explore(self):
        """
        Returns True if teh agent should explore
        :return:
        """
        return self.exploration_on and self._generator.random() < self._epsilon

    def act(self, states):
        pass

    def train(self, history):
        pass