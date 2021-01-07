import numpy as np
import random
from players.player import Player


class MonteCarloPlayer(Player):

    def __init__(self):
        self._q = dict()
        self._return = dict()

    def act_from_state(self, board):
        afterstates = board.afterstates()
        if random.random() < 0.9:
            rewards = []
            for a in afterstates:
                if repr(a._board) in self._q:
                    rewards.append(self._q[repr(a._board)])
                else:
                    rewards.append(13)
            max_reward = max(rewards)
            # Break ties randomly so we could explore all the states
            index = [i for i in range(len(afterstates)) if rewards[i] == max_reward]
            return afterstates[random.choice(index)]
        else:
            return random.choice(afterstates)

    def update(self, moves, score):
        for m in moves:
            if repr(m) in self._return:
                self._return[repr(m)].append(score)
            else:
                self._return[repr(m)] = [score]
            self._q[repr(m)] = sum(self._return[repr(m)])/len(self._return[repr(m)])

