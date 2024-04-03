def code_with_comas(words: list) -> str:
    result = " "
    for word in range(len(words) - 1):
        result += str(words[word]) + " "
    result += str("i " + words[len(words) - 1])
    return result


words = ["jabłka", "banany", "tofu", "koty"]

print(code_with_comas(words))
