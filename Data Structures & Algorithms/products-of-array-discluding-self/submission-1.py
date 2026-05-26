class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0]*len(nums)

        for i in range(len(nums)): #一个指针对准当前位置
            product = 1
            for j in range(len(nums)): #另一个指针遍历所有不是当前位置的
                if i == j:
                    continue
                product *= nums[j]
            output[i] = product
        return output