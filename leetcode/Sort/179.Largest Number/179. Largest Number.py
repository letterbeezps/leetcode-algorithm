import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def mycmp(x, y):
            if x+y < y+x:
                return 1
            else:
                return -1
        
        largest_num = ''.join(sorted(map(str, nums), key=functools.cmp_to_key(mycmp)))
        
        return '0' if largest_num[0] == '0' else largest_num

###########################################################
class LargeNumKey(str):
    def __lt__(x,y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        largest_num = ''.join(sorted(map(str, nums), key=LargeNumKey))
        
        return '0' if largest_num[0] == '0' else largest_num