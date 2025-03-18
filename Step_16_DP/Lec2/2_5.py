class Solution:
    def rob(self, nums) -> int:
        # top down

        # if we are robbing house 1 we can't rob last house
        # total_houses = len(nums)
        # dp = [[-1 for _ in range(2)] for _ in range(total_houses)]
        # if total_houses<=3:
        #     return max(nums)

        # def max_rob(house_index, is_last_robbed):
        #     if house_index==0 and is_last_robbed==0:
        #         return nums[house_index]

        #     if house_index<=0:
        #         return 0
        #     if dp[house_index][is_last_robbed]!=-1:
        #         return dp[house_index][is_last_robbed]
            
        #     if house_index==total_houses - 1:
        #         #take last one 
        #         not_take = max_rob(house_index-1, False)
        #         take = nums[house_index]+max_rob(house_index-2, True)
        #         dp[house_index][is_last_robbed] = max(take,not_take)

        #     else:
        #         not_take = max_rob(house_index-1, is_last_robbed)
        #         take = nums[house_index]+max_rob(house_index-2, is_last_robbed)
        #         dp[house_index][is_last_robbed] = max(take,not_take)

            
        #     return dp[house_index][is_last_robbed]

     
        # return max_rob(total_houses-1, False)



        #bottom up
        total_houses = len(nums)
        
        if total_houses<=3:
            return max(nums)

        dp = [[0 for _ in range(2)] for _ in range(total_houses)]
        dp[0][0],dp[0][1] = 0,nums[0]
        dp[1][0],dp[1][1] = nums[1], nums[0]
        



        for i in range(2,total_houses):
            for j in range(2):
                if i==total_houses-1 and j==1:
                    dp[i][j] = max(dp[i-1][j],dp[i-2][j])
                    continue
                dp[i][j] = max(dp[i-1][j],dp[i-2][j]+nums[i])


            
        return max(dp[total_houses-1][0],dp[total_houses-1][1])