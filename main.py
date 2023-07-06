#!/usr/bin/env python3

# Перемножение матриц
# Если возможно перемножить - вывести результат
# Если невозможно - вывести сообщение от ошибке

from random import randint
from classes import matrix as mtrx

if __name__ == '__main__':
    print("Введите через пробел количество строк и столбцов матрицы\nПример: '2 3' означает матрицу 2х3")
    print("Квадратную матрицу можно задать одним числом")
    help_line = "Введите измерения матрицы"

    mtrxA = mtrx(input(help_line + " A: ").split())
    # mtrxB = mtrx(input(help_line + " B: ").split())

    # mtrxA.set_mtrx([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    mtrxA.set_mtrx([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # mtrxB.set_rand()

    # mtrxC = mtrxA.sum(mtrxB)
    # mtrxC = mtrxA.mult(mtrxB)

    print("A")
    mtrxA.print()
    # print("\nB")
    # mtrxB.print()
    # print("\nC")
    # mtrxC.print()

    print("\nA rotated")
    mtrxA.rotate()
    mtrxA.print()

    print("\nA rotated")
    mtrxA.rotate()
    mtrxA.print()