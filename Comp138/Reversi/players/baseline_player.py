import numpy as np
import random
import reversi


class BaselinePlayer:
    """
    An agent for a six by six reversi board
    make choice based on a pre-set reward matrix
    """

    def __init__(self, rewards):
        """
        Create the reward matrix for a board of size 6
        """
        # I modified the reward matrix since in the paper it is using a borad of size 8
        self._rewards = rewards

    def Choose_from_afterstates(self, reversi):
        """
        Choose the afterstates that maximize the rewards
        and change the state of the reversiboard
        :param reversi: a reversi board
        :return:
        """
        afterstates = reversi.afterstates()
        rewards = []
        for afterstate in afterstates:
            rewards.append(-np.sum(afterstate._board * self._rewards))
        max_reward = max(rewards)

        # Break ties randomly so we could explore all the states
        index = [i for i in range(len(afterstates)) if rewards[i] == max_reward]

        return afterstates[random.choice(index)]

    def act(self, states):
        return [self.Choose_from_afterstates(state) for state in states]

    def train(self, history):
        pass


if __name__ == '__main__':
    # To test functionality
    r = reversi.ReversiState(6)
    bp = baseline_player_size6()
    bp.Choose_from_afterstates(r)
    print(r._board)
    bp.Choose_from_afterstates(r)
    print(r._board)
    for i in range(33):
        bp.Choose_from_afterstates(r)
        print(r._board)



