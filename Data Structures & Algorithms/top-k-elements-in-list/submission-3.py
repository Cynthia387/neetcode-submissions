class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # 数字 : 出现的次数
        for n in nums:
            count[n] = 1 + count.get(n, 0) # count how many times the number occured in the list
        # convert to 数组(为了sort)
        arr = []
        for n, cnt in count.items(): # .items()返回键值对
            arr.append([cnt,n]) # 这里把频次放在前，目的是：频次最高排在数组最后，pop()从末尾拿最大元素无需挪动其他元素位置，时间复杂度o1
        arr.sort() # 按频率排序（sort是按第一个元素排序）
        
        result = []
        while len(result) < k: # 只要手机的答案个数还没达到k个，就一直从排序后的数组末尾拿元素
            result.append(arr.pop()[1]) # .pop()：第一次弹出整个[3,3]，再加上[1]就能弹出[cnt,n]这个小列表中代表数字本身的n
        return result

