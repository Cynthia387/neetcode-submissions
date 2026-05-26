class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        substr = set()
        l = 0 # l需要手动维护，r是for循环变量，会自动创建&每轮赋值

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            res = max(res, r-l+1)
        return res
        