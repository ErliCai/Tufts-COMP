from players.player import Player
from ..cnn import ReversiCNN


class DQNPlayer(Player):

    def __init__(self, size):
        """
        Create a Deep-Q-Learning Reversi player for a certain board size
        :param size: Size of the board for which to create an agent
        """
        super().__init__(size)
        # TODO

    def make_move(self, state):
        """
        Return the next state corresponding to the action taken by the player
        :param state: a ReversiState
        :return:      a ReversiState such that it is in state.afterstates()
        """
        # TODO