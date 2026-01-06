class Solution:
    def beautySum(self, s: str) -> int:
        from collections import Counter

        def beauty(sub):
            d = Counter(sub)
            a = list(d.values())
            if len(a) <= 1:
                return 0
            return max(a) - min(a)
        
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                res += beauty(s[i: j])

        return res