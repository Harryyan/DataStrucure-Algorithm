# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.
# Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jc = len(jobDifficulty)
        if d > jc: return -1
        dp = [[-1 for i in range(jc+1)] for i in range(d+1)]
        dp[1][1] = jobDifficulty[0]

        for i in range(2, jc+1):
            dp[1][i] = max(dp[1][i-1], jobDifficulty[i-1])
        
        for i in range(2, d+1):
            for j in range(i, jc+1):
                dp[i][j] = dp[i-1][j-1] + jobDifficulty[j-1]
                work = jobDifficulty[j-1]
                for k in range(j-2, i-2, -1):
                    work = max(jobDifficulty[k], work)
                    if dp[i-1][k] + work < dp[i][j]:
                        dp[i][j] = dp[i-1][k] + work
        return dp[d][jc]

jobDifficulty = [6,5,4,3,2,1]
d = 2

s = Solution()
r = s.minDifficulty(jobDifficulty,d)

print(r)