import json
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # 解法一
        # 题目给的是一个已经排序的数组
        l = len(nums)
        i = 0
        while i < l - 1:
            j = i + 1
            if nums[i] == nums[j]:
                nums.remove(nums[j])  # 如果后一个元素和前一个元素相同，则将其删除
                l -= 1
            else:
                i += 1
        return l
        """
        # 解法2 效率提升max
        l = len(nums)
        if l == 0:
            return 0
        
        index = 0  # index 用来记录新数组的索引
        i = 1
        while i < l:
            if nums[index] != nums[i]:
                nums[index+1] = nums[i]
                index = index + 1
            i += 1
        return index + 1

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
            
            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()