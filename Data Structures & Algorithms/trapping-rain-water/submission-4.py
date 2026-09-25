class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 1, len(height)
        prefixMax = [0]*len(height)
        suffixMax = [0]*len(height)
        bucket = 0
        prefixMax[0]=height[0]
        for i in range(left, right):
            prefixMax[i]=max(prefixMax[i-1],height[i])
        suffixMax[right-1]=height[right-1]
        for i in range(right-2, -1, -1):
            suffixMax[i]=max(suffixMax[i+1], height[i])
        for i in range(len(height)):
            bucket += min(prefixMax[i], suffixMax[i]) - height[i]
        return bucket