class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        brackets = {'(':')', '[':']', '{': '}'}
        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif char in brackets.values():
                if not stack: return False
                popcorn = stack.pop()
                if char == brackets[popcorn]:
                    continue
                else: return False
            else: return False
        if stack: return False
        else: return True            