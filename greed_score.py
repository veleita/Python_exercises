# Greed is a dice game played with five six-sided dice.
# Given five values of a six-sided dice, this function scores a throw according to these rules:
#
#   Three 1's => 1000 points
#   Three 6's =>  600 points
#   Three 5's =>  500 points
#   Three 4's =>  400 points
#   Three 3's =>  300 points
#   Three 2's =>  200 points
#   One   1   =>  100 points
#   One   5   =>   50 point

def score(dice):
    score = 0

    for value in dice:
        print(value)

    return score


# TESTS
print(score([5, 1, 3, 4, 1]))   # 250:  50 (for the 5) + 2 * 100 (for the 1s)
print(score([2, 4, 4, 5, 4]))   # 450:  400 (for three 4s) + 50 (for the 5)
print(score([1, 1, 1, 3, 1]))   # 1100: 1000 (for three 1s) + 100 (for the other 1)