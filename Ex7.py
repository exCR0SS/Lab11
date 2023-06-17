class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createHead(self):
        num = int(input("Введите число: "))
        while num != -1:
            new_node = Node(num)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            num = int(input("Введите число: "))

    def createTail(self):
        num = int(input("Введите число: "))
        while num != -1:
            new_node = Node