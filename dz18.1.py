def second_index(text, symbol):
    if text.count(symbol) > 1:
        return text.find(symbol, text.find(symbol) + 1)
    else:
        return None


print(second_index("sims", 's'))
print(second_index("find the river", 'e'))
print(second_index("hi", 'h'))