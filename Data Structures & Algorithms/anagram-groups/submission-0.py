class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newdict = {}
        for i in strs:
            count = Counter(i)

            key = tuple(sorted(count.items()))
            if key not in newdict:
                newdict[key] = []
            newdict[key].append(i) #if word matches count key, append to value pair
        return list(newdict.values())