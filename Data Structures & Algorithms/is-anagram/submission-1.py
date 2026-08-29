class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        if sCount == tCount: return True
        else: return False

        