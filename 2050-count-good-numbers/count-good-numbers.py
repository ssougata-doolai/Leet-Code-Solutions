MOD = 10 ** 9 + 7

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(a, b):
            if b == 0:
                return 1
            half = power(a, b // 2)
            if b % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * a) % MOD
        
        return (power(5, (n+1) // 2) * power(4, n // 2)) % MOD


        # memo = {}
        # def count(indx):
        #     if indx == n:
        #         return 1
            
        #     if indx in memo:
        #         return memo[indx]

        #     if indx % 2 == 0:
        #         memo[indx] = (5 * count(indx+1)) % MOD
        #     else:
        #         memo[indx] = (4 * count(indx+1)) % MOD
        #     return memo[indx]

        # return count(0)