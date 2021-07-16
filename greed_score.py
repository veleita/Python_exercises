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
    final_score = 0
    score_table = {1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0}

    for value in dice:
        if value in score_table.keys():
            score_table[value] += 1

    for key, value in score_table.items():
        if key == 1:
            if value >= 3:
                score_table[key] = 1000 + (value - 3) * 100
            elif value in range(1, 3):
                score_table[key] = 100 * value
        elif key == 5 and value in range(1, 3):
            score_table[key] = 50 * value
        elif value >= 3:
            score_table[key] = key * 100
        else:
            score_table[key] = 0
        final_score += score_table[key]

    return final_score


# TESTS
print(score([5, 1, 3, 4, 1]))   # 250:  50 (for the 5) + 2 * 100 (for the 1s)
print(score([2, 4, 4, 5, 4]))   # 450:  400 (for three 4s) + 50 (for the 5)
print(score([1, 1, 1, 3, 1]))   # 1100: 1000 (for three 1s) + 100 (for the other 1)
