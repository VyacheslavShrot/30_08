from typing import Callable


def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func: Callable) -> int:
    for n in range(end):
        yield begin
        begin = func(begin)




print(list(some_gen(2, 4, pow)))