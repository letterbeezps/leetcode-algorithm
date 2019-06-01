import json
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1  # 用来记录向前进位的数值
        l = len(digits)
        i = l - 1
        while i >= 0:
            if carry == 0:
                return digits
            tmp = carry + digits[i]  # 当前的最末位默认加一
            carry = tmp // 10  # 进位的数值
            digits[i] = tmp % 10  # 计算新的个位
            i -= 1
        if carry != 0:
            digits.insert(0,1)
        return digits

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
            digits = stringToIntegerList(line)
            
            ret = Solution().plusOne(digits)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()