# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def append(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(val)
        self.len += 1

    def insert(self, val, position):
        if self.len < position:
            print("impossible to insert")
            return
        current = self.head
        temp = Node(val)
        if position == 0:
            self.head = temp
            self.head.next = current
        else:
            for i in range(position-1):
                current = current.next
            temp.next = current.next
            current.next = temp
        self.len += 1

    def delete(self, position):
        current = self.head
        if position == 0:
            self.head = self.head.next
        else:
            for i in range(position - 1):
                current = current.next
            current.next = current.next.next

    def print_all(self):
        result = ''
        current = self.head
        while current is not None:
            result += str(current.val) + ' -> '
            current = current.next
        result += 'null'
        print(result)


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.insert(2, 2)
linked_list.print_all()
linked_list.delete(1)
linked_list.print_all()