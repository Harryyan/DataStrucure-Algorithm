from typing import List
import collections

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 
# a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。


# 解题思路1：排序 + 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            # 第一步去重，遇到相同的元素，直接跳过，避免重复
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    
                    # 同理，从左边起，若下一个元素和当前元素相同，跳到下一个；
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                        
                    # 同理，从右边起，若下一个元素和当前元素相同，跳到下一个；
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res

# 解题思路2： 字典 + 剪枝
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1

        keys = sorted(cnt.keys())
        res = []
        for i, a in enumerate(keys):
            # 处理相等的情况, cnt[a]-1是为了保证下面的b和c如果和a相等的话其cnt至少也需要为1
            cnt[a] -= 1
            for b in keys[i:]:
                if cnt[b] >= 1:
                    # 这里需要保证cnt[b]至少为1, 因为有可能a和b相等, 但是cnt[a]=1, 此时就不可以用b了
                    c = -a-b
                    if c < b:
                        # 剪枝优化, 后面的b更大, 意味着c更不满足c>=b了, 直接break即可
                        break
                    if c > b and cnt[c] >= 1 or c == b and cnt[b] >= 2:
                        # 去重考虑, 添加的三个数必须是非递减的关系
                        res.append([a, b, c])
        return res
    
nums = [-1,0,1,2,-1,-4]
s = Solution()

print(s.threeSum(nums))