class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        l, r = 0, 1 #为什么r是1不是len(prices)-1或是别的
        maxP = 0

        while r < len(prices): # while r is within the array
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit) # update maximum profit
            else: # if price at right is lower, then right becomes new left, because cheaper buying price is always better
                l = r
            r += 1
        return maxP