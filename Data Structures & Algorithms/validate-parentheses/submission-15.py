class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = {'(':')', '{':'}', '[':']'}
        if len(s)%2!=0: return False
        for char in s:
            if char in openBrackets.keys():
                stack.append(char)
            elif stack:
                if openBrackets[stack[-1]]==char: 
                    stack.pop()
                else: return False
            else: return False
        if stack: return False
        else: return True