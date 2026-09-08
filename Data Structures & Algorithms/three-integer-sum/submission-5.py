class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]: continue
            left = i+1
            right = len(nums)-1
            while left < right and i < right:
                if nums[left] + nums[right] == -nums[i]:
                    newList = [nums[i], nums[left], nums[right]]
                    if newList not in output: output.append(newList)
                    left+=1
                elif nums[left] + nums[right] > -nums[i]:
                    right-=1
                elif nums[left] + nums[right] < -nums[i]:
                    left+=1
                
        return output
            
            