class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointers：注意两次去重
        res = []
        nums.sort()

        for i, a in enumerate(nums): #这里用enumerate因为要一边遍历一边有下标
            if a > 0: #如果排序后这个数字大于0了，那剩下的也肯定都大于0，sum就不可能等于0
                break 

            if i > 0 and a == nums[i-1]: #去重，不然会得到重复的三元组
                continue # i > 0是为了防止i = 0时访问nums[-1]
                # 这里跳过用的是continue，因为当前循环由for控制，for循环会自己更新i所以不能写i += 1
                # 第一个数的去重是跳过一个循环，第二个数的去重是改变搜索区间
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([a, nums[l], nums[r]]) #这里append进去时不要忘了加[]（题目要求）；而且append只接收一个参数
                    r -= 1 #这里不动指针会卡死循环，而且为了保证下一次尝试新的组合
                    l += 1
                    while nums[l] == nums[l-1] and l < r: #第二个数的去重，这里还要加上l < r是因为python不会自动重新检查外层条件
                        l += 1
                        # 这里是由while控制的，指针的移动要手动维护；这里如果用continue会跳到while的下一轮，但l没变
        return res