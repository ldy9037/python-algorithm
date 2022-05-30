# 카카오 블라인드 - 뉴스 클러스터링
def sep(string):
    return list(filter(lambda s: s.encode().isalpha() and len(s) == 2, map(lambda i,s: s.lower() if i == (len(string) -1) else (s + string[i + 1]).lower() , range(len(string)), string)))

def solution(str1, str2):
    answer = 0
    
    str1 = sep(str1)
    str2 = sep(str2)

    same = 0

    for s in str1: 
        if s in str2: 
            str2.remove(s)
            same += 1
    
    answer = same / (len(str1) + len(str2)) if len(str1) != 0 or len(str2) != 0 else 1

    return int(answer * 65536)

str1 = "!@#$@!$!"
str2 = "!@@@@#@!"
print(solution(str1, str2))

