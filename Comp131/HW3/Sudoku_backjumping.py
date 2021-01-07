import numpy as np
from datetime import datetime

class Sudoku_Backjumping:

    def __init__(self, initial_values):
        self._grids = np.array(initial_values)
        self._grids_to_be_filled = self.grid_to_fill_in()

    def check_rows(self, p):
        r = p[0]
        c = p[1]
        v = self._grids[r,c]
        row = self._grids[r,:]
        for j in range(9):
            if self._grids[r,j] == v and j != c:
                return False

        return True

    def check_columes(self,p):
        r = p[0]
        c = p[1]
        v = self._grids[r,c]
        colume = self._grids[:, c]
        for j in range(9):
            if self._grids[j,c] == v and j != r:
                return False

        return True

    def check_regions(self, position):
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
        return self.check_columes(p) and self.check_rows(p) and self.check_regions(p)

    def grid_to_fill_in(self):
        To_be_filled = []
        for i in range(9):
            for j in range(9):
                if self._grids[i,j] == 0:
                    To_be_filled.append([i,j])
        return To_be_filled

    def solve(self):
        print(self._grids)
        To_be_filled = self.grid_to_fill_in()
        if not To_be_filled:
            print('answer')
            print(self._grids)
            quit()
            return True, None
        else:
            current_grid = To_be_filled[0]
            x = current_grid[0]
            y = current_grid[1]
            for i in range(10):
                if i == 9:
                    self._grids[x, y] = 0
                    print(x,y,self._grids)
                    return False, [x,y]
                self._grids[x, y] = i + 1
                if self.check([x,y]):
                    s = self.solve()
                    if not s[0]:
                        m = s[1][0]
                        n = s[1][1]
                        if (x == m or y == n or
                            ((m-(m%3) <= x < m-(m%3)+3) and
                             (n-(n%3) <= y < n-(n%3)+3))):
                            continue
                        else:
                            self._grids[x, y] = 0
                            return s






if __name__ == '__main__':
    start = datetime.now()

    # grids0 = [[6,9,8,7,5,2,1,3,4],
    #          [4,7,3,6,1,8,5,9,2],
    #          [1,2,5,4,3,9,8,6,7],
    #          [7,6,1,9,8,3,4,2,5],
    #          [3,8,2,5,4,1,9,7,6],
    #          [5,4,9,2,6,7,3,8,1],
    #          [8,0,0,0,0,6,7,5,0],
    #          [2,0,0,0,9,0,0,0,8],
    #          [0,0,6,8,0,5,2,0,3]]
    # s = Sudoku_Backjumping(grids0)
    # print(s.grid_to_fill_in())
    # s.solve()


    grids = [[6,0,8,7,0,2,1,0,0],
             [4,0,0,0,1,0,0,0,2],
             [0,2,5,4,0,0,0,0,0],
             [7,0,1,0,8,0,4,0,5],
             [0,8,0,0,0,0,0,7,0],
             [5,0,9,0,6,0,3,0,1],
             [0,0,0,0,0,6,7,5,0],
             [2,0,0,0,9,0,0,0,8],
             [0,0,6,8,0,5,2,0,3]]
    s = Sudoku_Backjumping(grids)
    print(s.grid_to_fill_in())
    s.solve()

    print()
    print()
    #
    # grids2 = [[0, 7, 0, 0, 4, 2, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 8, 6, 1, 0],
    #          [3, 9, 0, 0, 0, 0, 0, 0, 7],
    #          [0, 0, 0, 0, 0, 4, 0, 0, 9],
    #          [0, 0, 3, 0, 0, 0, 7, 0, 0],
    #          [5, 0, 0, 1, 0, 0, 0, 0, 0],
    #          [8, 0, 0, 0, 0, 0, 0, 7, 6],
    #          [0, 5, 4, 8, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 6, 1, 0, 0, 5, 0]]
    # s2 = Sudoku_Backjumping(grids2)
    # print(s2.grid_to_fill_in())
    # s2.solve()
    #
    # print(datetime.now() - start)
    #
    # print(s2._grids_to_be_filled)