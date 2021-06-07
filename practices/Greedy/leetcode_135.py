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
            
        if indexes[0] != 0:
            start = 0
            end = indexes[0]
            
            for j in range(end-1, start-1, -1):
                if ratings[j] > ratings[j+1]:
                    candies[j] = candies[j+1]+1    
                else:
                    if ratings[j] < ratings[j+1] and ratings[j+1]==1:
                        candies[j] = 1
                        for i in range(j, end):
                            if ratings[j+1]>ratings[j] and candies[j+1]<=candies[j]:
                                candies[j+1] = candies[j]+1
                    else:
                        candies[j] = candies[j+1]

        for i, index in enumerate(indexes):
            start = index
            end = indexes[i+1] if i < len(indexes) - 1 else len(indexes) - 1
            
            if start == end:
                break
            
            for j in range(start, end):
                x = j + 1 if j <= end - 1 else end
                
                if ratings[x] > ratings[j]:
                    candies[x] = candies[j]+1
                else:
                    if ratings[x] < ratings[j] and ratings[j] == 1:
                        ratings[x] = 1
                        for y in range(x-1,start,-1):
                            if ratings[y] > ratings[y+1] and candies[y] <= candies[y+1]:
                                candies[y] = candies[y+1]+1     
                    else:
                        candies[x]=1

        print(candies)
        return sum(candies)
        
    
    
sample = [1,3,2]
s = Solution()

print(s.candy(sample))