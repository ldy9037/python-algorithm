# 카카오 인턴쉽 - 표 편집
"""
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
"""

"""
linked_list 시작
"""
class LinkedList:
    def __init__(self):
        self.head = None

    def setHead(self, node):
        self.head = node

    def getHead(self):
        return self.head

    def length(self):
        result = 0
        current = self.getHead()

        while current != None:
            current = current.getLink()
            result += 1

        return result

    def add(self, index, node):             
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["index"] <= index:
            if current["index"] == index:
                node.setLink(current["node"])

                if prev == None: self.setHead(node)
                else: prev.setLink(node)
                break

            prev = current["node"]
            current["node"] = current["node"].getLink()                
            current["index"] += 1
        
        if current["index"] > index: return -1

    def addAfterValue(self, value, node):
        current = self.getHead()
        
        while current != None: 
            if current.getValue() == value: 
                node.setLink(current.getLink())
                current.setLink(node)
                break
            
            current = current.getLink()
        
        return -1

    def append(self, node):
        current = self.getHead()

        if current == None: 
            self.setHead(node)
            return

        while current != None:
            if current.getLink() == None: 
                current.setLink(node)
                break
            
            current = current.getLink()

    def remove(self, index): 
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["index"] <= index:
            if current["index"] == index:
                if prev == None: self.setHead(current["node"].getLink())
                else: prev.setLink(current["node"].getLink())
                return current["node"].getValue()
            
            prev = current["node"]
            current["node"] = current["node"].getLink()
            current["index"] += 1
        
        return None

    def removeByValue(self, value):
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["node"] != None:
            if current["node"].getValue() == value:
                prev.setLink(current["node"].getLink())
                return current["index"]

            prev = current["node"]
            current["node"] = current["node"].getLink() 
            
        return -1

    def getValue(self, index):
        current = {"index": 0, "node": self.getHead()}
        
        while current["node"] != None: 
            if current["index"] == index: return current["node"].getValue()

            current["node"] = current["node"].getLink()
            current["index"] += 1
        
        return None

    def toList(self):
        result = []

        current = self.getHead()
        while current != None: 
            result.append(current.getValue())
            
            current = current.getLink()
        
        return result

class Node:
    def __init__(self, value, link=None):
        self.value = value
        self.link = link

    def setLink(self, node):
        self.link = node
    
    def setValue(self, value):
        self.value = value
    
    def getLink(self):
        return self.link 
    
    def getValue(self):
        return self.value
"""
linked_list 끝
"""
def solution(n, k, cmd_list):
    answer = 'O' * n
    
    delete_stack = []
    selected = k    
    table = LinkedList()

    for i in range(n): table.append(Node(i))

    for cmd in cmd_list:
        if len(cmd) >= 2:
            direction, count = cmd.split()
            count = int(count)
            selected = selected - count if direction == "U" else selected + count
        if  len(cmd) == 1:
            if cmd == "C": 
                delete_stack.append((selected, table.remove(selected)))
                if selected >= table.length(): selected -= 1
            else: 
                index, value = delete_stack.pop()  

                if table.length() <= index: table.append(Node(value))
                else: table.add(index, Node(value))

                if index <= selected: selected += 1

    while delete_stack:
        index, value = delete_stack.pop()
        answer = answer[:value]+'X'+answer[value + 1:]
    
    return answer

n = 8
k = 2
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
cmd = ["U 2", "C","Z", "C","Z", "C","Z"]
#OOXOXOOO
print(solution(n, k, cmd))