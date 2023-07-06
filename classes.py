from dataclasses import dataclass
from random import randint

@dataclass
class matrix:
    ''' class for math operation with matrixes '''
    rows: int       # number of rows
    cols: int       # number of columns
    mtrx: list      # matrix itself

    def __init__(self, args):
        ''' if there is one argument - matrix is square '''
        self.rows = int(args[0])
        if not len(args) < 2:
            self.cols = int(args[1])
        else:
            self.cols = self.rows
        # generate matrix with 0 everywhere
        mtrx = []
        for i in range(self.rows):
            mtrx.append([])
            for j in range(self.cols):
                mtrx[i].append(0)
        self.mtrx = mtrx

    def set_mtrx(self, mtrx):
        self.rows = len(mtrx)
        self.cols = len(mtrx[0])
        self.mtrx = mtrx

    def set_rand(self):
        ''' generate random matrix '''
        mtrx = []
        for i in range(self.rows):
            mtrx.append([])
            for j in range(self.cols):
                mtrx[i].append(randint(0, 9))
        self.mtrx = mtrx

    def transp(self):
        ''' transpose matrix '''
        mtrx_res = matrix([self.cols, self.rows])
        mtrx_res.mtrx = [[row[i] for row in self.mtrx ] for i in range(len(self.mtrx[0]))]
        self.set_mtrx(mtrx_res.mtrx)

    def rotate(self):
        ''' rotate 90 grad clockwise '''
        mtrx_res = matrix([self.cols, self.rows])
        for row in range(self.rows):
            for col in range(self.cols):
                mtrx_res.mtrx[col][self.rows - row - 1] = self.mtrx[row][col]
        self.set_mtrx(mtrx_res.mtrx)

    def print(self):
        ''' Dummy func to print list '''
        print('\n'.join(str(row) for row in self.mtrx))

    def sum(self, mtrx_2nd):
        ''' returns matrix object that contains result of sum opertion '''
        if type(mtrx_2nd) != type(self):
            print(f"Argument must be matrix object, not '{type(mtrx_2nd)}'")
            return
        if self.rows != mtrx_2nd.rows or self.cols != mtrx_2nd.cols:
            print("Cannot sum matrix with different dimentions")
            return
        mtrx_res = matrix([self.rows, self.cols])
        for i in range(self.rows):
            for j in range(self.cols):
                mtrx_res.mtrx[i][j] = self.mtrx[i][j] + mtrx_2nd.mtrx[i][j]
        return mtrx_res
    
    def mult(self, mtrx_2nd):
        ''' returns matrix object that contains result of multiply opertion '''
        if type(mtrx_2nd) != type(self):
            print(f"Argument must be matrix object, not '{type(mtrx_2nd)}'")
            return
        if self.cols != mtrx_2nd.rows:
            print("Invalid matrixes for multiplication")
            return
        mtrx_res = matrix([self.rows, mtrx_2nd.cols])
        for i in range(self.rows):
            for j in range(mtrx_2nd.cols):
                for k in range(self.cols):
                    mtrx_res.mtrx[i][j] += self.mtrx[i][k] * mtrx_2nd.mtrx[k][j]
        return mtrx_res
