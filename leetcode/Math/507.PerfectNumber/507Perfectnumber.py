'''
所有真因子之和等于自身
看数据范围只能o(sqrt(n))了,num的因子最大不会超过sqrt(num)
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        i, sumn = 1, 0
        while i*i <= num:
            if num % i == 0:
                sumn += i
                if i*i != num:
                    sumn += num // i
            i += 1
        return (sumn - num) == num
                