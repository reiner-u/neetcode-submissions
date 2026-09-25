class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftWall, rightWall = height[left], height[right]
        bucket = 0
        while left < right:
            if leftWall < rightWall:
                left+=1
                leftWall = max(leftWall, height[left])
                bucket += leftWall-height[left]
            else:
                right -=1
                rightWall = max(rightWall, height[right])
                bucket += rightWall-height[right]
        return bucket
            