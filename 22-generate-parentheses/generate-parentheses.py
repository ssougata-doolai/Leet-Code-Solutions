class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(curr, op, cl, n, res):
            if len(curr) == n*2:
                res.append(curr)
                return
            if op < n:
                generate(curr + "(", op+1, cl, n, res)
            if cl < op:
                generate(curr + ")", op, cl+1, n, res)
        
        res = []
        generate("", 0, 0, n, res)
        return res

        # Brute Force
        # def is_valid(res):
        #     bal = 0
        #     for c in res:
        #         if c == "(":
        #             bal += 1
        #         else:
        #             bal -= 1
        #         if bal < 0:
        #             return False
        #     return bal == 0

        # def generate_all(p, n, res):
        #     if len(p) == n*2:
        #         if is_valid(p):
        #             res.append(p)
        #         return
        #     generate_all(p + "(", n, res)
        #     generate_all(p + ")", n, res)
        
        # def generate(n):
        #     res = []
        #     generate_all("", n, res)
        #     return res

        # return generate(n)
