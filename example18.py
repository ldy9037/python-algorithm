def korean_number(num):
    num_kr = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구', '십']

    return num_kr[num]
 
result = korean_number(int(input('숫자 입략 :')) - 1)
print(result)