num = int(input("숫자 입력 : "))
kr = ['영', '일', '이', '삼']

if num <= 3 and num >= 0:
    print(kr[num])
else: 
    print('숫자는 0이상 3이하로만 입력해주세요.')

