class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 还是 using sorted string as key
        # use defaultdict(list)自动为新key创建一个空列表，使代码更简洁
        hashmap = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())
            
        
