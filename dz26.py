import string

def first_word(text: str) -> str:
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    a = text.split()




    return a[0]



print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word("... and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))