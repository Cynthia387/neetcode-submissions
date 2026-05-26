class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0

        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0] #位置0左边最大高度=自己
        for i in range(1, n): #i=0已经算过，所以从1开始
            leftMax[i] = max(leftMax[i-1],height[i]) #左边之前最高vs当前高度
        
        rightMax[n-1] = height[n-1] #最后一个位置的右边最大值=自己
        for i in range(n-2, -1, -1): #n-1算过了，所以从n-2开始；stop边界不包含，所以写-1实际遍历到index=0
            rightMax[i] = max(rightMax[i+1],height[i]) 
        
        water = 0 #变量必须先定义
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        
        return water
        