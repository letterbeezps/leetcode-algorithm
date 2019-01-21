import json
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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