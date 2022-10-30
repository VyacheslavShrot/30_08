

#def prime(number: int) -> bool:
    #n = 2
    #while n < number // 2:
        #if number % n == 0:
            #return False
       # n = n + 1

    #return True


def prime_generator(a: int) -> int:

    def is_prime(number: int) -> bool:
        n = 2
        while n < number // 2 + 1:
            if number % n == 0:
                return False
            n = n + 1

        return True

    yield 2

    i = 3
    while i <= a:
        if is_prime(i):
            yield i

        i = i + 1

print(list(prime_generator(10)))
