class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumVal = []
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimumVal or val <= self.minimumVal[-1]:
            self.minimumVal.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minimumVal[-1]:
            self.minimumVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumVal[-1]
