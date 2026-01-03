class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        len_s = len(s)
        len_goal = len(goal)

        if len_s != len_goal:
            return False

        for i in range(len_s):
            s = s[1:] + s[0]
            if s == goal:
                return True

        return False 