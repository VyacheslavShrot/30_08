from typing import Union

def difference(*args) -> Union[int, float]:
    if len(args) == 0:
        return 0

    return float(max(args) - min(args))



print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())