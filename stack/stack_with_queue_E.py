from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft()) 

        item = self.q1.pop()
        self.q1 = self.q2
        self.q2 = deque()
        return item        

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft()) 

        return self.q1[0]        

    def empty(self) -> bool:
        return len(self.q1) == 0 
    
# implement stack by making push operation costly
class Stack:

    def __init__(self):

        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# with one queue
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        res = self.q[0]
        self.push(self.q.popleft())
        return res

    def empty(self) -> bool:
        return len(self.q) == 0
