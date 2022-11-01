from functools import cache
import time
import sys


def fat(n):
    if n == 1:
        return 1
    else:
        return n*fat(n-1)


@cache
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    x1 = 1
    x2 = 1
    for i in range(n):
        soma = x1 + x2
        x2 = x1
        x1 = soma

    return x1


def prime(n):
    pass


if __name__ == '__main__':
    sys.setrecursionlimit(50000)
    ini = time.time()
    print(fib(5))
    fim = time.time()
    print(fim - ini)
