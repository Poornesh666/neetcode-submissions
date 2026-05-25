class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mini = val

        if self.stack:
            mini = min(val, self.stack[-1][1])

        self.stack.append((val, mini))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]