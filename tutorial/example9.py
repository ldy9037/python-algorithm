num = int(input('숫자 입력 : '))
result = str(num)

if num >= 1000 and num <= 999999:
    result = str(num // 1000) + 'k'
elif num >= 1000000:
    result = str(num // 1000000) + 'M'

print(result)
