# 파이썬은 linked list가 없길래 그냥 간단하게 구현해 봄.(최소한의 기능만 포함)
# 필요한 기능은 그때그때 추가해서 사용할 것.
# 중복 코드가 조금 많음. 기능을 좀 더 잘게 나눠야 겠음.

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
        
        while current != None and current["index"] < index:
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
        self.connectNode(self.getTail(), node, None)

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
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
    
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
    
