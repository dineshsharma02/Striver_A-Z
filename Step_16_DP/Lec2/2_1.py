class Solution:
    def climbStairs(self, n: int) -> int:


        # 70. Climbing Stairs

        
        # top down memoization
        # dp = [-1]*(n+1)
        # def helper(n):
        #     if n<=2:
        #         return n
        #     if dp[n]!=-1:
        #         return dp[n]
        #     dp[n] = helper(n-1) + helper(n-2)
        #     return dp[n]
        # return helper(n)


        # bottom up 
        if n<=2:
            return n
        
        dp = [-1] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]