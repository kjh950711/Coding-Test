class Queue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.str = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.str.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a = self.str[0]
        self.str.remove(a)
        return a

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.str[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.str) == 0

q = Queue()
q.push(2)
q.push(4)
print(q.pop())
print(q.peek())
print(q.empty())
print(q.pop())
print(q.empty())