# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
# 你需要按照以下要求，帮助老师给这些孩子分发糖果：
# 每个孩子至少分配到 1 个糖果。
# 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        min_value = min(ratings)
        candies = [0] * len(ratings)
        
        # O(n)
        indexes = [i for i, x in enumerate(ratings) if x == min_value]
        
        # O(m)
        for index in indexes:
            candies[index] = 1
            
        if indexes[-1] < len(ratings)-1:
            indexes.append(len(ratings)-1)

        try:
            candies.index(0)
        except ValueError:
            return sum(candies)
        else:
            # 分区间计算
            # [0, 1st], [1st, 2nd], ..., [n-1,n]
            
            for i, index in enumerate(indexes):
                pre = indexes[i-1] if i > 0 else 0
                end = index
                
                for j in range(end, pre-1, -1):
                    if pre == 0:
                        if ratings[j-1] > ratings[j]:
                            candies[j-1] = candies[j] + 1
                        else:
                            candies[j - 1] = candies[j]
                    else:
                        if end - pre == 1:
                            if ratings[end] > ratings[pre]:
                                candies[end] = candies[pre] + 1
                            else:
                                candies[end] = candies[pre]
                        
                        if end - pre > 2:
                            if ratings[pre+1] <= ratings[end - 1]:
                                x = j + 1 if j < len(ratings)-1 else len(ratings)-1
                                if ratings[x] > ratings[j]:
                                    candies[x] = candies[j] + 1
                                else:
                                    candies[x] = candies[j]
                            else:
                                 if ratings[j-1] > ratings[j]:
                                    candies[j-1] = candies[j] + 1
                                 else:
                                    candies[j - 1] = candies[j]
                        else:
                            x = j + 1 if j < len(ratings)-1 else len(ratings)-1
                            if ratings[x] > ratings[j]:
                                candies[x] = candies[j] + 1
                            else:
                                candies[x] = candies[j]
        print(candies)
        return sum(candies)
        
    
    
sample = [1,0,2]
s = Solution()

print(s.candy(sample))