from typing import Dict, List

def popular_words(text: str, words: list) -> dict:
    a = {}

    text = text.lower().split()

    for n in words:
        a[n] = text.count(n)

    return a










print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))