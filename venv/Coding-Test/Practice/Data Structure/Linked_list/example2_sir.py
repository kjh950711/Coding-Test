## 리트코드 문제
# deleteDuplicates 함수
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


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


class Solution2:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.append(4)
linked_list.append(5)
linked_list.append(5)
linked_list.print_all()

solution = Solution2()
solution.deleteDuplicates(linked_list.head)

linked_list.print_all()
