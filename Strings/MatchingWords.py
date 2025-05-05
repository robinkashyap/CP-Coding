def matchingWord(words):
    dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in dict:
            dict[key] = [word]
        else:
            dict[key].append(word)
    return list(dict.values())

words = ['cat', 'ate', 'tac', 'can', 'nac', 'eat', 'sun']
result = matchingWord(words)

# Print the result
for group in result:
    print(group)