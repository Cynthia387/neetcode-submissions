class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using sorted string as key
        hashmap = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(s)
        return list(hashmap.values())

        