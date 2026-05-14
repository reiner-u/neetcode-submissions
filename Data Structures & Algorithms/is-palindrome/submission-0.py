class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(char for char in s if char.isalnum()).lower()
        newlist = ss[::-1]
        return (ss == newlist)
        
