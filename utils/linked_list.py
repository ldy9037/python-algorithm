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
            current = current.getLink()
            result += 1

        return result

    def add(self, index, node):             
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["index"] <= index:
            if current["index"] == index:
                node.setLink(current["node"])
                node.setNext(current["node"])
                node.setPrev(prev)

                if node.getNext() == None: self.setTail(node)
                else: current["node"].setPrev(node)

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
                node.setNext(current.getNext())
                node.setPrev(current)
                current.setLink(node)
                current.setNext(node)

                next_node = node.setNext()
                if next_node == None: self.setTail(node)
                else: next_node.setPrev(node)

                break
            
            current = current.getLink()
            current = current.getNext
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
    def __init__(self, value, link=None, next=None, prev=None):
        self.value = value
        self.link = link
        self.next = next
        self.prev = prev

    def setLink(self, node):
        self.link = node
    
    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def setValue(self, value):
        self.value = value

    def getLink(self):
        return self.link 
    
    def getNext(self):
        return self.next 

    def getPrev(self):
        return self.prev 

    def getValue(self):
        return self.value
    
