class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #双指针
        l, r = 0, len(numbers) - 1
        while l < r:
            cursum = numbers[l] + numbers[r]
            if cursum > target:
                r -= 1
            elif cursum < target: #这里一定要用elif，因为else只属于第二个if
                l += 1            #所以当三种情况互斥（只能发生一种时，一定要elif）
            else:
                return [l + 1, r + 1] #因为题目要求1-indexed，所以返回答案时要加上
        return []
        
                
        