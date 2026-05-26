class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 #为什么要初始化这个值，不能最后直接return max(res, sell - buy)
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)): #从i+1开始遍历，那不是会少遍历所有在i之前的值吗
                sell = prices[j]
                res = max(res, sell-buy)
        return res
        