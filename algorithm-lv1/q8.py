# 카카오 - [1차] 다트 게임
import re

def solution(dartResult):
    bonus = dict(zip('SDT*#', [1,2,3,2,-1]))

    number_list = list(map(int,re.findall(r'\d+', dartResult)))
    calc_list = re.findall(r'\D+', dartResult)
    
    for i in range(3):
        number_list[i] = number_list[i] ** bonus[calc_list[i][0]]
        if len(calc_list[i]) == 2: 
            number_list[i] *= bonus[calc_list[i][1]]
            if calc_list[i][1] == '*' and not i == 0: number_list[i-1] *= 2
        
    return sum(number_list)

dartResult = "1S2D*3T"
print(solution(dartResult))