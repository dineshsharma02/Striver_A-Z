class Solution:
    def minimizeCost(self, k, arr):
        # code here
        
        # top down memo
        # n = len(arr)
        # dp = [-1] * (n)
        
        # def get_min_cost(target_index):
        #     if target_index==0:
        #         return 0
                
        #     if dp[target_index]!=-1:
        #         return dp[target_index]
            
        #     ans = float("inf")
        #     for i in range(max(0,target_index-k), target_index):
        #         ans = min(ans, abs(arr[target_index]-arr[i]) + get_min_cost(i))
                
        #     dp[target_index] = ans
        #     return dp[target_index]
       
        # return get_min_cost(n-1)
        
        
        
        # bottom up
        n = len(arr)
        dp = [float("inf")] * (n)
        dp[0] = 0
        
        for i in range(1,n):
            
            for j in range(1,k+1):
                if i-j>=0:
                    dp[i] = min(dp[i], abs(arr[i]-arr[i-j]) + dp[i-j])
            
        return dp[n-1]