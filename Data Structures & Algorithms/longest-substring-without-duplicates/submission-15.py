class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        maxStreak = 0
        for index, letter in enumerate(s):
            if letter in hashmap:
                left = max(hashmap[letter] +1, left) 
            hashmap[letter] = index
            right = index+1
            if maxStreak < (right - left):
                maxStreak = right-left
        return maxStreak
