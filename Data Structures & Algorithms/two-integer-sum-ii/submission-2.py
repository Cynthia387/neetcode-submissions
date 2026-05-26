class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #hashmap 存储空间on，不符合要求
        mp = defaultdict(int) #不能设空list，不能做到o1查找
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in mp:
                return [mp[tmp], i+1] 
                # 这里的index是tmp的在前，因为hashmap存的是之前出现过的数，所以应是较小的index
            mp[numbers[i]] = i + 1 #numbers[i]指的是原list中i位置对应的值，mp[]指的是这个值在map中对应的位置index
        return []
                
        