'''
存在两个数a b，项全部异或求值得到a^b
a b不相同，即他们的二进制表示至少在某一位上不同
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = 0
        for x in nums:
            s ^= x  # s是其中两个数的异或，且这两个是数不一样
        
        k = 0
        while not(s >> k & 1):
            k += 1  # 在第k位，两个数开始不一样，非0即1
            
        s1 = 0
        for x in nums:
            if x >> k & 1:  # 将第k位上位1的数求出来
                s1 ^= x
                
        return [s1, s1^s]