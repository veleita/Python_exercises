# We are given a string in lowercase.
# We will treat each of its letters as people.
# The aim of the exercise is to replicate the wave effect, so that the return of the function
# is a list of strings creating a sequence in which the people of the initial string 'stand up'
# (turn to uppercase) in order

def wave(people):
    return [people[:index] + people[index].upper() + people[index + 1:] for index in range(0, len(people)) if people[index].isalpha()]

print(wave("hello"))
