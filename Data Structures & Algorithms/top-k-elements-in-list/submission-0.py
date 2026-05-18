class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostNums = Counter(nums)
        return [number for number, count in mostNums.most_common(k)]
