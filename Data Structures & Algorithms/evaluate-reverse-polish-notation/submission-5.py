class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        first = None
        second = None
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except:
                first = stack.pop()
                second = stack.pop()
                if i == '+':
                    stack.append(first + second)
                elif i == '-':
                    stack.append(second-first)
                elif i == '/':
                    stack.append(int(second/first))
                elif i == '*':
                    stack.append(first*second)
        return stack.pop()                                
