result = 0

while True:
    num = int(input('숫자 입력: '))

    if num >= 0:
        result += num
    else:
        print(result)
        break