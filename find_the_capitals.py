text = input()

def capital_indexes(text):
    return [i for i, char in enumerate(text) if char.isupper()]
print (capital_indexes(text))