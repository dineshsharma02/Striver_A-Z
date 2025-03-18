class Solution:
    def minCost(self, height):
        #top down 
        # n = len(height)
        # dp = [-1] * (n+1)
        # def get_min_cost(i):
        #     if i==0:
        #         return 0
        #     elif i==1:
        #         return abs(height[i]-height[0])
        #     if dp[i]!=-1:
        #         return dp[i]
            
        #     dp[i] =  min(abs(height[i]-height[i-1])+get_min_cost(i-1), abs(height[i]-height[i-2])+get_min_cost(i-2))
        #     return dp[i]
            
        # return get_min_cost(len(height)-1)
        
        
        #bottom up
        
        n = len(height)
        if n==1:
            return 0
            
        dp = [-1]*(n)
        dp[0] = 0
        dp[1] = abs(height[1]-height[0])
        dp[2] = abs(height[2]-height[0])
        
        for i in range(3,n):
            dp[i] = min(abs(height[i]-height[i-1]) + dp[i-1], abs(height[i]-height[i-2]) + dp[i-2])
            
        return dp[n-1]