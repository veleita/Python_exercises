def make_dict(list_of_tuples):
    return dict((key, value) for key, value in list_of_tuples)

users = make_dict([("Mariví", 30), ("Paco", 34), ("Anastasia", 45), ("Fatima", 26)])
print(users)


def register_repetitions(text):
    dict = {}
    list_of_words = text.split(" ")
    for word in list_of_words:
        dict[word] = list_of_words.count(word)
    return dict


print(register_repetitions("uno dos dos tres tres tres cuatro cuatro cuatro cuatro"))