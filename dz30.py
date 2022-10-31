
#def is_even(number: int) -> bool:

    #number = str()
    #for i in number:
        #if i[-1] == 0 or 2 or 4 or 6 or 8:

            #return True
        #else:

            #return False


def is_even(number: int) -> bool:

    number = str(number)

    return number[-1] in '24680'



print(is_even(2494563894038**2))
print(is_even(1056897**2))
print(is_even(24945638940387**3))
