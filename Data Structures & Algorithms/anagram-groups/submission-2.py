class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # don't have to deal with 1 edge case
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s) # list cannot be keys (mutable), so change to a tuple
        return list(result.values())


        