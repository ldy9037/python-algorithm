import unittest
from linked_list import LinkedList
from linked_list import Node

class TestLinkedList(unittest.TestCase):

    l_list = None

    def setUp(self):
        self.l_list = LinkedList()

    def test_then(self):
        print("- 노도가 5개 세팅 되어 있을 때")
        
        for i in range(5):
            self.l_list.append(Node(i, None, None))

        self.assertEqual(self.l_list.length(), 5, "노드가 정상적으로 세팅되지 않았습니다.")

    def tearDown(self):
        print('[현재 Linked List 내부] : ', self.l_list.toList())
        
if __name__ == '__main__':
    unittest.main()