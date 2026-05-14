class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates1 = sorted([x for x in candidates if x <= target])
    
        def backtrack(start, comboList, target):
            if (target==0):
                combinations.append(comboList.copy())
                return
            for i in range(start, len(candidates1)):
                if i > start and candidates1[i] == candidates1[i-1]: continue
                remaining = target - candidates1[i]
                if candidates1[i]>target:break
                comboList.append(candidates1[i])
                backtrack(i+1, comboList, remaining)
                comboList.pop(-1)
            
        backtrack(0, [], target)
        return combinations        
            
            



        