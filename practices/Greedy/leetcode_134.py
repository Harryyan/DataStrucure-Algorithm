# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

# 说明: 

# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。


from typing import DefaultDict, List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        m = len(cost)
        result = -1
        start = -1
        
        for i in range(0, n):
            if gas[i] >= cost[i]: 
                start = i
                temp = 0
                result = start
                
                for j in range(start, n): 
                    gas_1 = gas[j]
                    gas_2 = gas[j+1 if j < n-1 else n-1] 
                    if j == n - 1: gas_2 = 0
                    
                    cost_1 = cost[j]
                    cost_2 = cost[j+1 if j < n-1 else n-1] 
                    if j == n - 1: cost_2 = 0

                    temp += gas_1 + gas_2 - cost_1 - cost_2

                    if temp >= 0: result = i; break
                    else: result = -1; temp = 0; break
                else:
                    result = -1
                  
                if result != -1:
                    for x in range(0, start):
                        gas_1 = gas[x]
                        # gas_2 = gas[x+1 if start-1 else start-1]
                        # if j == start - 1: gas_2 = 0
                    
                        cost_1 = cost[x]
                        # cost_2 = cost[x+1 if x < start-1 else start-1
                        # if j == start - 1: cost_2 = 0
                    
                        temp += gas_1 - cost_1 
                        
                        if temp < 0: break
                        
                if result != -1:
                    break
            else:
                temp = 0        
        
        return result
    
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

s = Solution()

print(s.canCompleteCircuit(gas,cost))