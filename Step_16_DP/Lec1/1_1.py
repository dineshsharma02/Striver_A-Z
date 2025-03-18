class Solution:
    
    def topDown(self, n):
        # Code here
        dp = [-1]*(n+1)
        MOD = 7 + (10)**9
        def helper(n):
            if n==0 or n==1:
                return n
            if dp[n]!=-1:
                return dp[n]
            dp[n] =(helper(n-1)+ helper(n-2))%MOD
            return dp[n]
        return helper(n)
            
    def bottomUp(self, n):
        # Code here
        prev1 = 0
        prev2 = 1
        MOD = 7 + (10)**9
        if n==0 or n==1:
            return n
        for i in range(2,n+1):
            current = (prev1 + prev2) % MOD
            prev1 = prev2
            prev2 = current
        return current