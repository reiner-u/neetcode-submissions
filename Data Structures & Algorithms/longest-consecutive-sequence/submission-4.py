class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == [0]:
            return 1
        if not nums:
            return 0
        longest = 0
        tally = 1
        numbers = sorted(set(nums))
        if numbers == [0]:
            return 1
        currentNum = numbers[0]
        for i in range(1, len(numbers)):
            if currentNum+1 == numbers[i]:
                currentNum = numbers[i]
                tally += 1
            elif (currentNum+1!=numbers[i]):
                currentNum = numbers[i]
                tally = 1
            if tally > longest:
                longest = tally
        return longest
