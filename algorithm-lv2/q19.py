# 2019 카카오 블라인드 - 오픈채팅방
from collections import defaultdict

def solution(record_list):
    answer = []
    
    message = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    nickname = defaultdict(str)
    histories = []

    for record in record_list:
        action = record.split()
        
        if action[0] != "Leave" : nickname[action[1]] = action[2]
        if action[0] != "Change": histories.append((action[1], action[0]))

    for id, action in histories:
        answer.append(nickname[id] + message[action])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
print(solution(record))