class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = start ^ goal
        count = 0
        while x != 0:
            x = x & (x-1)
            count += 1
        return count