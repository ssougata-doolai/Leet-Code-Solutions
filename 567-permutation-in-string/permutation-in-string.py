class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        str1 = sorted(s1)
        str1 = ''.join(str1)
        flag = False
        for i in range(l2 - l1 + 1):
            str2 = sorted(s2[i:i+l1])
            str2 = ''.join(str2)
            if str1 == str2:
                flag = True
                break

        return flag


        