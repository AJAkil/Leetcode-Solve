from collections import deque


class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s2) + len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# implement queue by making push operation costly
class MyQueue:

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0
    


class MyQueue:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.append(x)


    def pop(self) -> int:
        if len(self.s) == 0:
            return -1

        x = self.s.pop()

        if len(self.s) == 0:
            return x
        
        item = self.pop()

        self.s.append(x)

        return item
    

    def peek(self) -> int:
        if len(self.s) == 0:
            return -1

        x = self.s.pop()

        if len(self.s) == 0:
            self.s.append(x)
            return x

        item = self.peek()

        self.s.append(x)

        return item
