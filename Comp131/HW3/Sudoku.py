import numpy as np
from datetime import datetime


class Sudoku:

    def __init__(self, initial_values):
        """
        :param initial_values: initial values on the gridd
        """
        self._grids = np.array(initial_values)

    def check_rows(self, p):
        """
        check if there is conflict in the row
        :param p: postion we want to check
        """
        r = p[0]
        c = p[1]
        v = self._grids[r,c]
        row = self._grids[r,:]
        for j in range(9):
            if self._grids[r,j] == v and j != c:
                return False

        return True

    def check_columes(self,p):
        """
        check if there is conflict in the column
        :param p: postion we want to check
        """
        r = p[0]
        c = p[1]
        v = self._grids[r,c]
        colume = self._grids[:, c]
        for j in range(9):
            if self._grids[j,c] == v and j != r:
                return False

        return True

    def check_regions(self, position):
        """
        check if there is conflict in the 3 by 3 region
        :param p: postion we want to check
        """
        x0 = position[0]
        y0 = position[1]
        v = self._grids[x0,y0]
        x = x0 - (x0%3)
        y = y0 - (y0%3)

        for i in range(3):
            for j in range(3):
                if self._grids[x+i,y+j] == v and (x+i != x0 or y+j != y0):
                    return False
        return True

    def check(self, p):
        """
        check row, column an 3 by 3 region simultaneously
        """
        return self.check_columes(p) and self.check_rows(p) and self.check_regions(p)

    def grid_to_fill_in(self):
        """
        :return: coordinates of grid that are initially empty
        """
        To_be_filled = []
        for i in range(9):
            for j in range(9):
                if self._grids[i,j] == 0:
                    To_be_filled.append([i,j])
        return To_be_filled

    def solve(self):
        """
        solve the sudoku
        and print the answer
        """
        To_be_filled = self.grid_to_fill_in()
        if not To_be_filled:
            print('answer')
            print(self._grids)
            return True
        else:
            current_grid = To_be_filled[0]
            x = current_grid[0]
            y = current_grid[1]
            for i in range(10):
                if i == 9:
                    self._grids[x, y] = 0
                    return False
                self._grids[x, y] = i + 1
                if self.check([x,y]):
                    if not self.solve():
                        continue





if __name__ == '__main__':
    start = datetime.now()

    grids = [[6,0,8,7,0,2,1,0,0],
             [4,0,0,0,1,0,0,0,2],
             [0,2,5,4,0,0,0,0,0],
             [7,0,1,0,8,0,4,0,5],
             [0,8,0,0,0,0,0,7,0],
             [5,0,9,0,6,0,3,0,1],
             [0,0,0,0,0,6,7,5,0],
             [2,0,0,0,9,0,0,0,8],
             [0,0,6,8,0,5,2,0,3]]
    s = Sudoku(grids)
    s.solve()

    grids2 = [[0, 7, 0, 0, 4, 2, 0, 0, 0],
             [0, 0, 0, 0, 0, 8, 6, 1, 0],
             [3, 9, 0, 0, 0, 0, 0, 0, 7],
             [0, 0, 0, 0, 0, 4, 0, 0, 9],
             [0, 0, 3, 0, 0, 0, 7, 0, 0],
             [5, 0, 0, 1, 0, 0, 0, 0, 0],
             [8, 0, 0, 0, 0, 0, 0, 7, 6],
             [0, 5, 4, 8, 0, 0, 0, 0, 0],
             [0, 0, 0, 6, 1, 0, 0, 5, 0]]
    s2 = Sudoku(grids2)
    s2.solve()

    print(datetime.now() - start)

