class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = float('inf')
        

    def push(self, val: int) -> None:
        self.curr_min = min(val, self.curr_min)
        node = Node(val, self.curr_min)
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0 :
            self.curr_min = float('inf')
        else:
            self.curr_min = self.stack[-1].b

    def top(self) -> int:
        return self.stack[-1].a
        

    def getMin(self) -> int:
        return self.stack[-1].b


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()