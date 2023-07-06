#!/usr/bin/env python3

from random import randint
from classes import matrix as mtrx

if __name__ == '__main__':
    print("Введите через пробел количество строк и столбцов матрицы\nПример: '2 3' означает матрицу 2х3")
    print("Квадратную матрицу можно задать одним числом")
    help_line = "Введите измерения матрицы"

    mtrxA = mtrx(input(help_line + " A: ").split())
    mtrxB = mtrx(input(help_line + " B: ").split())

    mtrxA.set_rand()
    mtrxB.set_rand()

    print("A")
    mtrxA.print()
    print("\nB")
    mtrxB.print()

    if mtrxA.rows == mtrxB.rows and mtrxA.cols == mtrxB.cols:
        mtrxC = mtrxA.sum(mtrxB)
        print("\nA + B")
        mtrxC.print()

    if mtrxA.cols == mtrxB.rows:
        mtrxC = mtrxA.mult(mtrxB)
        print("\nA * B")
        mtrxC.print()

    print("\nA transposed")
    mtrxA.transp()
    mtrxA.print()
    mtrxA.transp()

    print("\nA rotated")
    mtrxA.rotate()
    mtrxA.print()

