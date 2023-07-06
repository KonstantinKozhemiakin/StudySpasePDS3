def is_palindrom(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrom(word[1:-1])


def is_palindrom_2(word):
    for i in range(len(word)):
        if (word[i] == word[-(i + 1)]):
            continue
        else:
            return False
    return True


print(is_palindrom("pololop"))
print(is_palindrom_2("pololop"))
