class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        return (len(nums) != len(set(nums)))
