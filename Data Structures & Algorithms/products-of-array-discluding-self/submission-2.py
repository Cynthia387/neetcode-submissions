class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #division，但要注意不能除以0
        #含0的array情况：2个，1个，没有
        countZero = 0
        prod = 1
        for num in nums:
            if num: #这句会把num当作布尔值判断
                prod *= num
            else:
                countZero += 1
        if countZero > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums) #构造结果数组
        for i, c in enumerate(nums): #遍历每个位置，包含下标i和current值
            if countZero: #等于if countZero != 0，这道题目里相当于=1了，因为>1的情况上面单独讨论过了
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res


    