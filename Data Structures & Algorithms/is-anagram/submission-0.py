class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(map(str, s))
        tt = list(map(str, t))
        ss.sort()
        tt.sort()
        if ("".join(ss)=="".join(tt)):
            return True
        else: return False
