class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 当前位置答案 = 左边所有数乘积 * 右边所有数乘积
        res = [1]*len(nums) # 作为乘积init为0不成立
        prefix = 1 # 左边
        for i in range(len(nums)):
            res[i] = prefix # 把左边乘积写进去
            prefix *= nums[i] # 把当前数乘进去
        postfix = 1 # 右边
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res