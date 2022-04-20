from functools import reduce

print(reduce(lambda x, y: x+y, range(5)))
print(reduce(lambda x, y: y+x, '12345'))

print(list(filter(lambda x: x<5, range(10))))
print(list(filter(lambda x: x%2 == 1, range(10))))