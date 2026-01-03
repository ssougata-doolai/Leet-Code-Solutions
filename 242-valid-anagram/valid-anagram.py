class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        d1, d2 = {}, {}

        for ch1, ch2 in zip(s, t):
            d1[ch1] = d1.get(ch1, 0) + 1
            d2[ch2] = d2.get(ch2, 0) + 1
        
        if d1 == d2:
            return True
        return False
        
        # if s.sort() == t.sort():
        #     return True
        # return False