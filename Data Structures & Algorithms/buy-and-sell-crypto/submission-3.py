class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming
        maxP = 0
        minBuy = prices[0] # 第一天唯一可能的买入价格就是 prices[0]

        for sell in prices: # 假设今天卖出
            maxP = max(maxP, sell-minBuy) #计算今天卖的利润&更新最大利润
            minBuy = min(minBuy, sell) # 更新历史最低买入价
        return maxP