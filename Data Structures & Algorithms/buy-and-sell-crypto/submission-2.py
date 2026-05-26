class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming
        maxP = 0
        minBuy = prices[0] # 为什么需要initialize这个

        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell) 
        return maxP