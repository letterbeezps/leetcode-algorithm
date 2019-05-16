'''
只与最后一个元素0的前面的连续1的个数有关系
'''
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        indexlast, count = len(bits)-2, 0
        while indexlast >= 0 and bits[indexlast] == 1:
            count += 1
            indexlast -= 1
        return True if count%2 == 0 else False