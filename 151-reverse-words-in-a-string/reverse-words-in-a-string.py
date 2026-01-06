class Solution:
    def reverseWords(self, s: str) -> str:
        a = []
        for item in s.split():
            a.append(item)
        a.reverse()
        return " ".join(a)
