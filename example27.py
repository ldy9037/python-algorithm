def sumOfDigits(num):    
    return sum(map(lambda x: int(x), str(num)))

print(sumOfDigits(22))