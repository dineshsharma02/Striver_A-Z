class Solution:
    def rob(self, nums) -> int:
        # top down approach
        # n = len(nums)
        # dp = [-1]*(n)
        # def max_rob(house_index):
        #     if house_index>=len(nums):
        #         return 0
        #     if dp[house_index]!=-1:
        #         return dp[house_index]
            
        #     dp[house_index] = max(nums[house_index] + max_rob(house_index+2), max_rob(house_index+1))
        #     return dp[house_index]
            
        
        # return max_rob(0)


        # bottom up
        total_houses = len(nums)
        if total_houses<=2:
            return max(nums)
        dp = [-1]*total_houses
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])


        for i in range(2,total_houses):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return dp[total_houses-1]