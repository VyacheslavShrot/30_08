def second_index(text, symbol):
    if text.find(symbol) == True:
        if text.find(symbol, text.find(symbol) + 1) == True:
            l = text.find(symbol)
            text = text.find(symbol, l + 1)
        else:
            return None
    else:
        return None
    return text





print(second_index("sims", 's'))
print(second_index("find the river", 'e'))
print(second_index("hi", 'h'))