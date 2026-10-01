class Solution:
    from collections import Counter 
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        left, maxFreq, result = 0,0,0
        right = len(s)-1
        for index in range(len(s)):
            if s[index] not in charCount: charCount[s[index]] = 1
            else: charCount[s[index]] +=1

            maxFreq = max(maxFreq, charCount[s[index]])

            while (index-left+1)-maxFreq > k:
                charCount[s[left]] -=1
                left+=1
            result = max(index-left+1, result)
        return result