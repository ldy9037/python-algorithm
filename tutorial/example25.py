def sumOfDigits(num):
    result = 0
    
    for char in str(num):
        result += int(char)

    return result

print(sumOfDigits(int(input('숫자를 입력 : '))))