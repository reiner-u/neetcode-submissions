class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        carMap = sorted([(position,speed) for position,speed in zip(position,speed)], reverse=True)
        fleets = 0
        for i in carMap:
            time = (target-i[0])/i[1]
            if stack and stack[-1] >= time:
                continue
            else: stack.append(time)
        return len(stack) 
