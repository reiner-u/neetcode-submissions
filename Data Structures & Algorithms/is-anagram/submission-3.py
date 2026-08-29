class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
#        sCount = Counter(s)
 #       tCount = Counter(t)
#        if sCount == tCount: return True
#        else: return False
        sMap = {}
        count = 1
        for i in s:
            if i in sMap:
                sMap[i] += 1
            else: sMap[i] = 1
        tMap = {}
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else: tMap[i] = 1       
        if tMap == sMap: return True
        else: return False
        