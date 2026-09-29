class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
            #Wrong btw this is not binary search lmaoooo fast asf tho
