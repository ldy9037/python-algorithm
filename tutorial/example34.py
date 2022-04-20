dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

result = set()

"""
for dice in dice1:
    result = result | set(map(lambda pr: dice + pr, dice2))
"""
for d1 in dice1:
    for d2 in dice2:
        result.add(d1 + d2)

print(result)