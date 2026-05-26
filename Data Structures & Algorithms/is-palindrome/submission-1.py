class Solution:
    def isPalindrome(self, s: str) -> bool:
        #这个办法会build a new string
        newstr = ""
        for c in s:
            if c.isalnum(): 
                newstr += c.lower()
        return newstr == newstr[::-1]
        