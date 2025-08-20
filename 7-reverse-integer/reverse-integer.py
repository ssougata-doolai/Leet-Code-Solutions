class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        flag = 0

        if x < 0:
            x *= -1
            flag = 1
        while x != 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10

        if flag == 1:
            rev *= -1
        if rev < -2147483648 or rev > 2147483647:
            return 0
        return rev
        