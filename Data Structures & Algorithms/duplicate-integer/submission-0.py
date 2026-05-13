class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        for i in nums:
            if i in new_list:
                return True
            new_list.append(i)
        return False