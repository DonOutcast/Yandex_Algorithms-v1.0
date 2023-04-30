def words_in_dict(dictionary, text):
    good_words = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            good_words.add(word[:delpos] + word[delpos + 1 :])
    ans = []
    for word in text:
        ans.append(word in good_words)
    return ans


