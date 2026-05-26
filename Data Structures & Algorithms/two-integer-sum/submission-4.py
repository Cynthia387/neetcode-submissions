class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这道题的hashmap设计是反向映射的value：key，
        ## 因为思维方式是我先知道一个value，想知道有没有diff=target-value，如果有，想知道它的index
        # every previous element is to be stored in this map, val:index
        prevMap = {}
        for i, n in enumerate(nums): # index, actual number
            diff = target - n
            # check if the diff is already in the hashmap
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return