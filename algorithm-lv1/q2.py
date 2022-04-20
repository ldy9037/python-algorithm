# 카카오 - 신규 아이디 추천
import re

def solution(new_id):
    answer = re.sub(r'[^a-z0-9-_.]', '', new_id.lower())

    while '..' in answer: answer = answer.replace('..', '.')        
    answer = answer.strip('.')
    if not answer: answer = 'a'
    if len(answer) >= 16: answer = answer[:15].rstrip('.')
    while len(answer) < 3: answer += answer[-1]
    
    print(answer)

    return answer

txt = "z-+.^."
solution(txt)