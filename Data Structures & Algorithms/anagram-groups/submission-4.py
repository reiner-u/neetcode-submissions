class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in strs:
            counted = Counter(i)
            key = tuple(sorted(counted.items()))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(i)
        return list(dictionary.values())

            
            