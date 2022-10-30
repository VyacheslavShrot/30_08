

def generate_cube_numbers(number:int) -> int:
    n = 2
    while n ** 3 < number:
        yield n ** 3
        n = n + 1

print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))

