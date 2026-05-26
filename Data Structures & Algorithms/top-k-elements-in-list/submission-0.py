class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # frequency : number
        for n in nums:
            count[n] = 1 + count.get(n, 0) # count how many times the number occured in the list
        
        arr = []
        for n, cnt in count.items(): # .items()什么用法
            arr.append([cnt,n]) # 这步也没看懂
        arr.sort()

        result = []
        while len(result) < k: # 为什么是小于不是等于k时
            result.append(arr.pop()[1]) # .pop()又是什么用法，为什么还有个1
        return result

