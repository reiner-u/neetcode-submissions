class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nilResult = -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            print (f"Mid Index: {mid}, Value: {nums[mid]}")
            if nums[left] == target:
                return left
            elif nums[mid] == target:
                return mid
            elif nums[right] == target:
                return right
        
            if nums[mid]>=nums[right]:
                if nums[mid] > target and nums[left] < target: 
                    right = mid-1
                else: left=mid+1
            else:
                if nums[mid] < target and nums[right] > target: left = mid+1 
                else: right = mid-1
        return nilResult    
            