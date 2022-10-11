#greetings, friends

import string
def correct_sentence(sentence1):
    sentence1 = sentence1[0].upper() + sentence1[1:]

    if sentence1[-1] != '.':
        sentence1 = f"{sentence1}."
    return sentence1

print(correct_sentence("greetings, friends."))
print(correct_sentence("Greetings, friends."))





