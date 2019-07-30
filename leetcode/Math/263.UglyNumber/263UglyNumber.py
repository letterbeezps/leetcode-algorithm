class Solution:
    def isUgly(self, num: int) -> bool:
        d = [2, 3, 5]
        for prime in d:
            while num > 0 and num % prime == 0:
                num //= prime 
        return num == 1