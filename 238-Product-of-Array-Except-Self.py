# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
    
#         length = len(nums)
#         left_mult = 1
#         right_mult = 1
#         left_arr = [0] * len(nums)
#         right_arr = [0] * len(nums)
#         for i in range(length):
#             j = -i -1
#             left_arr[i] = left_mult
#             left_mult *= nums[i]
#             right_arr[j] = right_mult
#             right_mult *= nums[j]
#         ans = [left_arr[i] * right_arr[i] for i in range(length)]
#         return ans

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(length-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]