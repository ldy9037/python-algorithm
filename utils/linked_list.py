# 파이썬은 linked list가 없길래 그냥 간단하게 구현해 봄.(최소한의 기능만 포함)
# 필요한 기능은 그때그때 추가해서 사용할 것.
# 중복 코드가 조금 많음. 기능을 좀 더 잘게 나눠야 겠음.
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

    def addNode(self, index, node):             
        current = {"index": 0, "node": self.getHead()}
        prev = None

        while current["index"] <= index:
            if current["index"] == index:
                node.setLink(current["node"])

                if prev == None: self.setHead(prev)
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
                break
            
            prev = current["node"]
            current["node"] = current["node"].getLink()
            current["index"] += 1
        
        if current["index"] > index: return -1

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
