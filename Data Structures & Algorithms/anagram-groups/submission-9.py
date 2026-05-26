class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using character count as key
        hashmap=defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1 # 不同字母减去ord('a')(a的编号)得到不同的index，比如c就会得到2，这一句就相当于index是2的count+1
         # Use tuple of counts as key
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())