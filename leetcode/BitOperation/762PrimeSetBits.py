'''
L 和 R 是小于10^6, 2^20是大于10^6的
L和R的二进制表示是不超过20位的，一般的操作控制在10^7最佳
'''
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = [2,3,5,7,11,13,17,19]
        
        res = 0
        for i in range(L, R+1):
            s = 0
            k = i
            while k:
                s += k & 1
                k >>= 1
            #end_while
            if primes.count(s):
                res += 1
        #end_for
        return res
        