# 카카오 블라인드 - 가사 검색
from collections import defaultdict

def solution(words, queries):
    answer = [0] * len(queries) 

    trie = defaultdict(int)
    trie_reverse = defaultdict(int)
    for word in words:
        for i in range(1, len(word) + 1):
            trie[word[:i]] += 1
            trie_reverse[word[-i:]] += 1

    print(trie_reverse)

    for i in range(len(queries)):
        query = queries[i]
        front = (query[0] == "?")
        
        query = query.replace("?", "")
        
        if front: answer[i] = trie_reverse[query]
        else: answer[i] = trie[query]

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]	
print(solution(words, queries))

# [3, 2, 4, 1, 0]
