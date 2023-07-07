# Napisz funkcję która otrzyma w parametrze listę stringów, a na wyjściu zwróci listę w postaci <slowo> <ilość liter>


words = ["ala", "ma", "kota", "i", "psa"]

def fun(x):
    result = []
    for word in x:
        result.append(f'{word} {len(word)}')
    return result              
    
result = fun(words)

print(result)








