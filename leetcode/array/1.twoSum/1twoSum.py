# -*- coding: utf-8 -*-
import json
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rs = [-1, -1]
        
        # dict为一个哈希表，以“目标和当前值得差”为索引，当前值得索引为值
        dict = {}
        l = len(nums)
        if l <= 1:
            return rs
        for i in range(l):
            if nums[i] in dict:
                rs[0] = dict[nums[i]]
                rs[1] = i
                return rs
            else:
                dict[target - nums[i]] = i # 目标值与当前值的“差”为键，当前值在num中的索引为字典里的“值”
        return rs

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()