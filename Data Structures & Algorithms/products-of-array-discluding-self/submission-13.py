class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        output[0]=1
        suffix=1
        for i in range(1, len(nums)):
            output[i] = output[i-1]*nums[i-1]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        return output
