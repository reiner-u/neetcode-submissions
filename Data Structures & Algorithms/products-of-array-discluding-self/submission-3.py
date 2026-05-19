class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in nums:
            items = nums.copy()
            items.remove(i)
            if 0 in items:
                products.append(0)
            else:
                products.append(math.prod(items))
        return products