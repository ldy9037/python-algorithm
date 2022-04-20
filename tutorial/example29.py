num = int(input('숫자 입력 : '))
result = []

while num != 0:
    share, remain = divmod(num, 2)
    result.insert(0, remain)
    num = share

"""
strBinary = bin(num).replace('0b', '')
result = list(map(lambda binary: int(binary), strBinary))
"""


print(result)