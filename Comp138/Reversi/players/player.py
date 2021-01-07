class Player:
    """ An abstract class to be extended by different Rerversi players"""

    def __init__(self, size):
        """
        Create a Reversi player for a certain board size
        :param size: size of the Reversi board
        """
        pass

    def make_move(self, state):
        """
        Return the next state corresponding to the action taken by the player
        :param state: a ReversiState
        :return:      a ReversiState such that it is in state.afterstates()
        """
        pass