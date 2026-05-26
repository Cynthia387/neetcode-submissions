class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        size, result=[], ''
        for s in strs:
            size.append(len(s)) #把每个字符串的长度记录下来，生成的是list[]
        for sz in size:
            result += str(sz) #把长度列表变成字符串str
            result += ','
        result += '#' #长度区的终止符
        for s in strs:
            result += s #把所有字符串直接拼接起来
        return result
        #因为已经知道每个str的长度了，decode时会按照长度分割，所以可以直接全部拼接

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size, result, i = [],[], 0
        while s[i] != '#': #读长度列表，读到长度区终止符为止
            
            cur = ''
            while s[i] != ',': #读到不是逗号的，就往cur里加进去
                cur += s[i]
                i+=1 #指针挪到逗号
            size.append(int(cur)) #变成长度列表
            i += 1 #指针跳过逗号
        i += 1 #跳过#，进入内容区
        for sz in size: #按照每个长度size，切整的内容区str
            result.append(s[i:i + sz])
            i += sz
        return result
        
