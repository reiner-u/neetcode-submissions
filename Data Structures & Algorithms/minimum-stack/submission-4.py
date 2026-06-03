class MinStack:

    def __init__(self):
        self.minimumStack = []
        return

    def push(self, val: int) -> None:
        self.minimumStack.append(val)

    def pop(self) -> None:
        self.minimumStack.pop()

    def top(self) -> int:
        return self.minimumStack[-1]

    def getMin(self) -> int:
        copiedStack = sorted(self.minimumStack)
        return copiedStack[0]
