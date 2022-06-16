import unittest
from linked_list import LinkedList
from linked_list import Node

class TestLinkedList(unittest.TestCase):

    l_list = LinkedList()

    def setUp(self):
        print("- Then: 노드가 5새 세팅되어 있을 때")

        for i in range(5):
            self.l_list.append(Node(i, None, None))

    def tearDown(self):
        print('[현재 Linked List 내부] : ', self.l_list.toList())

    def test_when(self):    
        self.assertEqual(self.l_list.length(), 5, "노드가 정상적으로 세팅되지 않았습니다.")

        print("- When: 3번째 위치(index = 2)에 값이 0인 노드를 삽입하고")
        self.l_list.add(2, Node(0))
        self.assertEqual(self.l_list.length(), 6, "노드가 정상적으로 삽입되자 않았습니다.")
        self.assertEqual(self.l_list.findNodeByIndex(2).getValue(), 0, "노드가 잘못된 위치에 삽입되었습니다.")
        
if __name__ == '__main__':
    unittest.main()