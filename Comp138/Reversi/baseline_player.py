import numpy as np
import random
import reversi

class baseline_player_size6:
    """
    An agent for a six by six reversi board
    make choice based on a pre-set reward matrix
    """

    def __init__(self):
        """
        Create the reward matrix for a board of size 6
        """
        # I modified the reward matrix since in the paper it is using a borad of size 8
        self._rewards = np.array([
            [100, -25, 10,10, 25, 100],
            [-25, -25, 5, 5, -25, -25],
            [10,  5, 1, 1, 5, 10],
            [10,  5, 1, 1, 5, 10],
            [-25, -25, 5, 5, -25, -25],
            [100, -25, 10, 10, -25, 100],
        ])


    def Calculate_total_reward(self, state):
        """
        :param state: represent the state on the reversi board
        :return: int representing total reward
        """
        reward = 0
        for i in range(6):
            for j in range(6):
                #minus sign here since board is already flipped in after state
                reward -= self._rewards[i,j] * state[i,j]
        return reward


    def Choose_from_afterstates(self, reversi):
        """
        Choose the afterstates that maximize the rewards
        and change the state of the reversiboard
        :param reversi: a reversi board
        :return:
        """
        afterstates = reversi.afterstates()
        rewards = []
        if afterstates is None:
            reversi._board = - reversi._board
        else:
            for afterstate in afterstates:
                rewards.append(self.Calculate_total_reward(afterstate))
            max_reward = max(rewards)

            # Break ties randomly so we could explore all the states
            index = [i for i in range(len(afterstates)) if rewards[i] == max_reward]
            reversi._board = afterstates[random.choice(index)]
            reversi._remaining_steps -= 1




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


