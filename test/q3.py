# 카카오 인턴쉽 - 표 편집

"""
"U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
"D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
"C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
"Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.
"""

"""
linked_list by ldy9037@naver.com
"""
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        self.head = node

    def setTail(self, node):
        self.tail = node

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def length(self):
        result = 0
        current = self.getHead()

        while current != None:
            current = current.getNext()
            result += 1

        return result

    def connectNode(self, prev, current, next):
        current.setPrev(prev)
        current.setNext(next)

        if current.getNext() == None: self.setTail(current)
        else: current.getNext().setPrev(current)

        if current.getPrev() == None: self.setHead(current)
        else: current.getPrev().setNext(current)

    def disconnectNode(self, prev, next):
        if prev == None: self.setHead(next)
        else: prev.setNext(next)

        if next == None: self.setTail(prev)
        else: next.setPrev(prev)

    def findNodeByIndex(self, index):
        current = {"index": 0, "node": self.getHead()}
        
        while current["node"] != None and current["index"] < index:
            current["index"] += 1
            current["node"] = current["node"].getNext()

        return current["node"]        

    def findNodeByValue(self, value):
        current = self.getHead()

        while current != None and current.getValue() != value:
            current = current.getNext()

        return current

    def add(self, index, node):             
        current = self.findNodeByIndex(index)
        if current == None: return False
        
        self.connectNode(current.getPrev(), node, current)

        return True

    def addAfterValue(self, value, node):
        current = self.findNodeByValue(value)
        if current == None: return False
        
        self.connectNode(current, node, current.getNext())

        return True

    def append(self, node):
        if self.getTail() == None: self.setTail(node)
        else: 
            self.getTail().setNext(node)
            node.setPrev(self.getTail())
            self.setTail(node)
        #self.connectNode(self.getTail(), node, None)

    def remove(self, index): 
        current = self.findNodeByIndex(index)
        if current != None: self.disconnectNode(current.getPrev(), current.getNext())
        
        return current

    def removeByValue(self, value):
        current = self.findNodeByValue(value)
        if current != None: self.disconnectNode(current.getPrev(), current.getNext())

        return current

    def getValue(self, index):
        result = None

        current = self.findNodeByIndex(index)
        if current != None: result = current.getValue()
        
        return result

    def toList(self):
        result = []

        current = self.getHead()
        while current != None: 
            result.append(current.getValue())
            
            current = current.getNext()
        
        return result

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setValue(self, value):
        self.value = value
    
    def getNext(self):
        return self.next 

    def getPrev(self):
        return self.prev 

    def getValue(self):
        return self.value

"""
linked list 끝
"""

def solution(n, k, cmd_list):
    answer = ['O'] * n
    
    delete_stack = []
    move = 0
    table = LinkedList()

    next_n = None
    c = Node(0, None, None)
    for i in range(n): 
        if i == 0: table.setHead(c)
        if i == k: selected = c
        if i == n - 1:table.setTail(c)
        else: 
            next_n = Node(i + 1, c, None)
            c.setNext(next_n)
            c = next_n

    for cmd in cmd_list:
        if len(cmd) >= 2:
            direction, count = cmd.split()
            count = int(count)
            move = move - count if direction == "U" else move + count
        if  len(cmd) == 1:
            for i in range(abs(move)):
                selected = selected.getPrev() if move < 0 else selected.getNext()
            
            move = 0

            if cmd == "C": 
                table.disconnectNode(selected.getPrev(), selected.getNext())
                delete_stack.append(selected)

                selected = selected.getNext() if selected.getNext() != None else selected.getPrev()
            else: 
                node = delete_stack.pop()
                table.connectNode(node.getPrev(), node, node.getNext())

    while delete_stack:
        node = delete_stack.pop()
        answer[node.getValue()] = 'X'
    
    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd = ["U 2", "C","Z", "C","Z", "C","Z"]
#OOXOXOOO
print(solution(n, k, cmd))