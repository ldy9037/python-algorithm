# 카카오 블라인드 - 가사 검색

# http://github.com/ldy9037
class Trie:
    def __init__(self):
        self.head = Node("")

    def save(self, string):
        length = len(string)
        current = self.head

        current.getLength().append(length)

        for c in string: 
            next = current.nextNode(c)
            if next == None:
                next = Node(c)
                current.getNext()[c] = next
            
            next.getLength().append(length)
            current = next
        
    def find(self, string):
        current = self.head
        for c in string:
            if current == None: break
            current = current.nextNode(c)
            
        return current

class Node:
    def __init__(self, key):
        self.key = key
        self.next = {}
        self.length = []

    def nextNode(self, key):
        if key in self.next: 
            return self.next[key]

        return None

    def getLength(self):
        return self.length

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next        

def solution(words, queries):
    answer = [0] * len(queries) 

    trie = Trie()
    trie_reverse = Trie()

    for word in words:
        trie.save(word)
        trie_reverse.save("".join(reversed(word)))

    for i, query in enumerate(queries):
        length = len(query)
        node = trie.find(query.replace("?","")) if query[-1] == "?" else trie_reverse.find(query.replace("?",""))
        
        if node: 
            answer[i] = node.getLength().count(length)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "??????", "pro?"]	
print(solution(words, queries))

# [3, 2, 4, 1, 0]
