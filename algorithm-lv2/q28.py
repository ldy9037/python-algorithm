# 카카오 인턴십 - 튜플
def solution(s):
    answer = []

    s_set = sorted(list(map(lambda subset: subset.replace("{", "").replace("}", ""), s.split("},{"))),key=lambda x: len(x))

    for subset in s_set: 
        subset = subset.split(",") 

        for r in answer: subset.remove(str(r))

        answer.append(int(subset[0]))

    return answer

s = "{{20},{2120,20,202020},{2120,20}}"
print(solution(s))

#[2, 1, 3, 4]

"""
아주 마음에 드는 풀이가 있었음.
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter
"""
