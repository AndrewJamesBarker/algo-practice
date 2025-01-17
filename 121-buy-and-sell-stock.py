# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         a,b = 0,1
#         P = len(prices)
#         max_profit = 0
#         while b < P:
#             if prices[a] < prices[b]:
#                 max_profit = max(max_profit, prices[b] - prices[a])
#             else:
#                 a = b
#             b += 1
#         return max_profit
    
# print(Solution().maxProfit([7,1,5,3,6,4])) # 5

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
    
print(Solution().maxProfit([7,1,5,3,6,4])) # 5