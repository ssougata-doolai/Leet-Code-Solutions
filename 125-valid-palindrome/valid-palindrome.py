class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch for ch in s if ch.isalnum()).lower()
        l = len(s)
        flag = True
        for i in range(l//2):
            if s[i] != s[l-1-i]:
                flag = False
                break
        
        return flag
        