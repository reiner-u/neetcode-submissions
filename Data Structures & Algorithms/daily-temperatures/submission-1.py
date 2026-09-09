class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]: 
                popcorn = stack.pop() 
                result[popcorn] = i-popcorn #we calculate the day in which we found a warmer temp (popcorn) and subtract from it the current day (i) 
            stack.append(i) #we keep adding to the stack here
        return result