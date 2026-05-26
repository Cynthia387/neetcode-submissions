class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #哈希解法的思想：不是通过位置关系，二是通过数值关系判断连续
        s=set(nums) #去重，建立O(1)查找结构（哈希表）
        #括号里的nums表示用nums里的所有元素初始化一个set，等价于建立一个空set之后通过一个遍历把nums中的数都加进这个set
        best=0 #记录目前找到的最长连续序列的长度
        for x in s:
            if x-1 not in s: #当x是序列起点的时候开始数，并保证不会重复扩展（比如x=3的时候，因为x-1=2已经在set中，所以会直接跳过）
                y=x
                while y in s: #检查的是下一个数是否存在，而非下一个位置是什么
                    y+=1
                best = max(best,y-x)
        return best

        