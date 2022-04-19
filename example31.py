def korean_number(num):
    num_kr = {1: '일', 2: '이', 3:'삼', 4:'사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    return num_kr[num]

print(korean_number(int(input('숫자 입력 : '))))