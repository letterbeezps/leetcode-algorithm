import json
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l == 0:
            return 0
        dp = 0
        minprice = prices[0]
        for i in range(1, l):
            dp = max(dp, prices[i] - minprice)
            minprice = min(prices[i], minprice)
        return dp

def stringToIntegerList(input):
    return json.loads(input)

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
            prices = stringToIntegerList(line)
            
            ret = Solution().maxProfit(prices)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()


"""
在控制台执行代码
zp-MACdeMacBook-Pro:List zpmac$ python3 121maxProfit.py
接着输入数组
[7, 1, 5, 3, 6, 4]
5
[7, 6, 4, 3, 1]
0
"""