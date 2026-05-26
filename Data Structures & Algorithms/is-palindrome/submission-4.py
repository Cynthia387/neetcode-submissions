class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            #分别过滤左右非alnum字符
            if not s[l].isalnum():
                l += 1
                continue #continue会立刻回到while开头重新检查，等价于自动重复执行
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
