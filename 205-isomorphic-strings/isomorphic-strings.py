class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        visited1 = {}
        visited2 = {}
        
        for i in range(n):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in visited1:
                if visited1[ch1] != ch2:
                    return False
            else:
                if ch2 in visited2:
                    return False
                visited1[ch1] = ch2
                visited2[ch2] = ch1
        return True

            