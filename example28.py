max = 30
numArr = list(range(2, max + 1))
prIndex = 0

while prIndex + 1 <= len(numArr):
    pr = numArr[prIndex]
    
    numArr = list(filter(lambda num: num == pr or num % pr != 0, numArr))
    prIndex += 1

print(numArr)