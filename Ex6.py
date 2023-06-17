class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, N):
        self.head = None
        for i in range(N, 0, -1):
            new_node = Node(i)
            new_node.next = self.head
            self.head = new_node

    def removeEverySecondElement(self):
        temp = self.head
        while temp is not None and temp.next is not None:
            next_node = temp.next.next
            temp.next = next_node
            temp = next_node

    def getLastElement(self):
        return self.head.data