class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        currentMax = 0
        while left<right:
            container = (right-left)*(min(heights[left], heights[right]))
            if currentMax < container: currentMax = container
            if heights[left] < heights[right]:
                left+=1
            else: right-=1
        return currentMax