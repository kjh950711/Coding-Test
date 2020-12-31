class Stack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.str = []

    # Data의 입력 (리스트의 append)
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.str.append(x)

    # Data의 출력 (리스트의 pop)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 방법1
        # return self.str.pop()

        #방법2
        num = self.str[-1]
        self.str.remove(num)
        return num

    def top(self) -> int:
        """
        Get the top element.
        """
        list = self.str
        return list[len(list)-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.str) == 0: a = True
        else: a = False
        return a

s = Stack()
s.push(1)
s.push(5)
s.push(8)
print(s.pop())
print(s.top())
print(s.empty())
print(s.pop())
print(s.pop())
print(s.empty())