def rebuild_sentence(words, lengths):

    rebuilt_array = []

    for i in range (len(words)):
        len(words[i]) == lengths[i]
        rebuilt_array.append(words[i])

    return rebuilt_array

words = ["The", "sky", "is", "blue"]
lengths = [3,2,2,1]

rebuild_sentence(words, lengths)
