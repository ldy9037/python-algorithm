# 카카오 블라인드 - 가사 검색
from collections import defaultdict

def solution(words, queries):
    answer = [0] * len(queries) 

    trie = dict()
    trie_reverse = dict()
    for word in words:
        word_length = len(word)
        if not word_length in trie:
            trie[word_length] = defaultdict(int)
            trie_reverse[word_length] = defaultdict(int)

        trie_reverse[word_length][""] += 1

        for i in range(1, word_length + 1):
            trie[word_length][word[:i]] += 1
            trie_reverse[word_length][word[-i:]] += 1

    for i in range(len(queries)):

        query_length = len(queries[i])
        if not query_length in trie: continue
        query = queries[i]
        front = (query[0] == "?")
        
        query = query.replace("?", "")

        if front: answer[i] = trie_reverse[query_length][query]
        else: answer[i] = trie[query_length][query]
 
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "??????", "pro?"]	
print(solution(words, queries))

# [3, 2, 4, 1, 0]
