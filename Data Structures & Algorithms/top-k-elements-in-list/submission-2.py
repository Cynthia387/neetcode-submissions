class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # 数字 : 出现的次数
        for n in nums:
            count[n] = 1 + count.get(n, 0) # count how many times the number occured in the list
        # convert to 数组
        arr = []
        for n, cnt in count.items(): # .items()返回键值对
            arr.append([cnt,n]) 
        arr.sort() # 按频率排序（sort是按第一个元素排序）
        
        result = []
        while len(result) < k: # 为什么是小于不是等于k时
            result.append(arr.pop()[1]) # .pop()会移除并返回列表最后一个元素
        return result

