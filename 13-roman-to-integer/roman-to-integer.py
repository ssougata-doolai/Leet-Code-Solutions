class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {
            'M': 1, 'D': 2, 'C': 3, 'L': 4, 'X': 5, 'V': 6, 'I': 7
        }

        d2 = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
        }

        prio = 1
        val = 0
        res = 0
        for ch in s:
            if d1[ch] < prio:
                res -= val
                res += d2[ch] - val
            else:
                res += d2[ch]
                prio = d1[ch]
                val = d2[ch]

        return res