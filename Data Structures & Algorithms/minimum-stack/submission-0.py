class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        min_int = self.stack[-1]
        temp = []
        while len(self.stack)!=0:
            min_int = min(min_int,self.stack[-1])
            temp.append(self.stack.pop())
        while len(temp)!=0:
            self.stack.append(temp.pop())
        return min_int
        
