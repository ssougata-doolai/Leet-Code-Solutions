class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        if l == 0:
            return ""
        
        if l == 1:
            return strs[0]

        n = len(strs[0])
        for i in range(1, l):
            x = len(strs[i])
            if x < n:
                n = x

        for i in range(n):
            ch = strs[0][i]
            for j in range(l):
                if strs[j][i] != ch:
                    return strs[0][:i]
        
        return strs[0][:n]