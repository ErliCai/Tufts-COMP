from reversi import ReversiState
from players.baseline_player import BaselinePlayer
import numpy as np


def play(starting_state, max_moves, players, n_games, games_in_batch, keep_score):
    """
    Play n_games games between two players. Half of the games the first agent
    statrs, the other half of the game the second player starts
    :param starting_state:  the state from which to start each game
    :param moves:           maximum number of moves in a game
    :param players:         a tuple of two reversi players
    :param n_games:         total number of games to play
    :param games_in_batch:  number of games to play simultaneously
    :param keep_score:  If true, keep track of who wins in every game and return
                        the result as described below
    :return:
    """
    assert (n_games % games_in_batch == 0)
    assert ((n_games // games_in_batch) % 2 == 0)
    batch = 0
    results = []
    while n_games > 0:
        curr = np.array([None] * (games_in_batch * max_moves))
        curr = np.resize(curr, (max_moves, games_in_batch))
        finished = np.array([None] * (games_in_batch * max_moves))
        finished = np.resize(finished, (max_moves, games_in_batch))
        curr[0, ] = starting_state
        moves = 0  # number of moves made
        while curr.shape[1] != 0:
            moves += 1
            curr[moves, :] = players[(moves + batch) % 2].act(curr[moves-1])
            if moves < 3:
                continue
            i = 0
            while i < curr.shape[1]:
                if curr[moves][i] != curr[moves-2][i]:
                    i += 1
                    continue
                score = curr[moves][i].get_score()
                results.append(([score[(moves + batch) % 2], score[(moves + batch + 1) % 2]]))
                # else = game over
                finished[:, games_in_batch - curr.shape[1]] = curr[:, i]
                curr = np.delete(curr, i, 1)
        players[batch % 2].train(finished[::2, ])
        players[batch % 2].train(finished[1::2, ])
        batch += 1
        n_games -= games_in_batch
    return np.array(results)


if __name__ == "__main__":
    player1 = BaselinePlayer([[100, -25, 10, 10, 25, 100],
                             [-25, -25, 5, 5, -25, -25],
                             [10,  5, 1, 1, 5, 10],
                             [10,  5, 1, 1, 5, 10],
                             [-25, -25, 5, 5, -25, -25],
                             [100, -25, 10, 10, -25, 100]])
    player2 = BaselinePlayer([[0]*6]*6)
    results = play(ReversiState(6),64, (player1, player2),
               n_games=20, games_in_batch=1, keep_score=True)

    print(np.sum(results[:, 0]),  np.sum(results[:, 1]) )
