class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = curr_len =  0
        l = 0
        for r in range(len(s)):
            while s[r] in seen: 
                seen.remove(s[l])
                l += 1
                curr_len -= 1
            seen.add(s[r])
            curr_len += 1
            max_len = max(curr_len, max_len)
        return max_len



        