class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # ans = [0] * len(nums)
        # i = 0
        # length = len(nums)
        # while i < length:
        #     product = 1
        #     j = 0
        #     for j in range(length):
        #         if j != i:
        #             product *= nums[j]
        #             ans[i] = product
        #     i += 1
        # return ans
    
        length = len(nums)
        left_mult = 1
        right_mult = 1
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)
        

print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]