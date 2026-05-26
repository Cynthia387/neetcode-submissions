class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set() #自动去重
        nums.sort() #不排序，会变成不同的tuple，set认为他们不同，sort可以让相同三元组长得一样，正确去重
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i],nums[j],nums[k]])) 
                        #这里加上tuple，因为set中的元素必须hashable，list是不能放进set的
        return [list(i) for i in res] 
        # 这里用外层一个中括号，而不是list()，因为res = {(-1,0,1), (-1,-1,2)}，是set[tuple]
            # 如果用list()，得到[(-1,0,1), (-1,-1,2)]，里面依然是tuple
            # 所以要用list comprehension逐个转换
        #这句是list comprehension，等价于：
            # ans = []
            # for i in res:
            #   ans.append(list(i))
            # return ans