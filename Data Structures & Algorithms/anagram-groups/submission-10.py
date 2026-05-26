class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting + hashmap
        # 还是 using sorted string as key
        # use defaultdict(list)自动为新key创建一个空列表，使代码更简洁
        hashmap = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s)) #排序后的s字符串作为key
            #dict中的key必须hashable，比如list是mutable（可变）的，就不能作key
            #tuple immutable，所以可以做key
            #还可以作key的是排序后的字符串：key = ''.join(sroted(s))
            hashmap[key].append(s) #同样的单词加入对应分组list
        return list(hashmap.values()) #返回所有分组，也就是hashmap中的values，外层用list包住（按题目要求）
            
        
