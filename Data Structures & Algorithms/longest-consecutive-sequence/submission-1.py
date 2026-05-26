class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #哈希解法：通过数值关系（+1是否在集合中）判断连续
        num_set = set(nums) # 转为set去重
        max_len = 0 #记录目前找到的最长连续序列的长度
        
        for num in num_set:
            # 只从序列起点开始数
            if num-1 not in num_set: # -1不在set中，说明是起点（这样保证不会重复扩展）
                current = num
                length = 1
                while current + 1 in num_set: # 不断检查下一个数是否在集合里
                    current += 1
                    length += 1     # 累积长度
                max_len = max(max_len,length)
        return max_len

        