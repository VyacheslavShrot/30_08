import string

def is_palindrome(text: str) -> bool:
    text = text.lower().replace(' ', '')

    for n in string.punctuation:
        text = text.replace(n, '')

    a = text == text[::-1]
    return a




print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('0P'))
print(is_palindrome('a.'))