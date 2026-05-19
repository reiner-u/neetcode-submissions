class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [math.prod(nums[:i] + nums[i+1:]) for i, value in enumerate(nums)]
        return products