# DFS/BFS - 단어 변환
# BFS 사용. 
# 문제 조건 확인 잘하자 ㅜ
from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((0, begin))

    if target in words:
        while queue:
            height ,begin = queue.popleft()
            words_temp = []

            while words:
                word = words.pop()
                
                duplicate_character = list(filter(lambda character: character[0] == character[1], zip(begin, word)))
                if len(begin) - len(duplicate_character) <= 1: 
                    if word == target: 
                        answer = height + 1
                        break
                    queue.append((height + 1, word))    
                else: words_temp.append(word)

            if answer != 0: break

            words = words_temp.copy()        
            
    return answer

begin = "hot"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))