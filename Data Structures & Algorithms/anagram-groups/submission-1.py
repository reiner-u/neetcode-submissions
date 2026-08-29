class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringDict = {}

        for i in strs:
            count = Counter(i)
            key = tuple(sorted(count.items()))
            if key not in stringDict:
                stringDict[key] = []
            stringDict[key].append(i)
        return list(stringDict.values())
            
            