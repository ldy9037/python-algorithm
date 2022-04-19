scoreArr = [0, 0, 2, 4, 7, 7, 9, 11, 11, 13, 18, 20]
stem_leaf = [[], [], []]

for score in scoreArr:
    share, remain = divmod(score, 10)
    
    stem_leaf[share].append(remain)

for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}')