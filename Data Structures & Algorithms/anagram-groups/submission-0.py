class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            if key not in result:
                result[key]=[]
            result[key].append(s)
        return list(result.values())