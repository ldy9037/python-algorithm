# 월간 코드 챌린지 - 음양 더하기
def solution(absolutes, signs):
    answer = 0

    for abs, sign in zip(absolutes, signs):
        answer = answer + abs if sign else answer - abs

    return answer

absolutes = [4,7,12]
signs = [True,False,True]

print(solution(absolutes, signs))

