def group_words(words) -> list[list]:
    groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = []
        groups[sorted_word].append(word)
    return list(groups.values())


print(group_words(["eat", "tea", "nat", "ate", "nat", "bat"]))
