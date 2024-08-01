def code_with_comas(words: list) -> str:
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        result = ", ".join(words[:-1])
        result += " i " + words[-1] 
        return result


words = ["jabłka", "banany", "tofu", "koty"]
words2 = ["jabłka"]

print(code_with_comas(words))
