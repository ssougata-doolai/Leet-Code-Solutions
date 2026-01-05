class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0

        for ch in s:
            if ch == "(":
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ")":
                depth -= 1
        
        return max_depth