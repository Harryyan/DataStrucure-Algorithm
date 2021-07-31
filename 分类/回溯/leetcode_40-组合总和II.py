from typing import List

# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 注意：解集不能包含重复的组合。 

class Solution:
    def combinationSum2(self,candidates, target):
        ans_all=[]
        candidates.sort()
        
        def dfs(candidates, resid, ans):
            if resid==0: ans_all.append(ans)
            if resid < 0: return
            n=len(candidates)
            i=0
            
            while i<n:
                dfs(candidates[i+1:n], resid-candidates[i], ans+[candidates[i]])
                j=i+1
                while j<n and candidates[j]==candidates[i]: j+=1
                i=j
        
        dfs(candidates, target, [])
        return ans_all

nums = [10,1,2,7,6,1,5]
target = 8
s = Solution()

r = s.combinationSum(nums, target)

print(r)