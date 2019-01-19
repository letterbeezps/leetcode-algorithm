import json
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        if len_prices < 2:
            return 0

        f = [0] * len_prices
        g = [0] * len_prices

        minf = prices[0]
        for i in range(1, len_prices):
            minf = min(minf, prices[i])
            f[i] = max(f[i-1], prices[i] - minf)

        maxg = prices[len_prices-1]
        for i in range(len_prices-1)[::-1]:
            maxg = max(maxg, prices[i])
            g[i] = max(g[i], maxg - prices[i])

        maxprofit = 0
        for i in range(len_prices):
            maxprofit = max(maxprofit, f[i] + g[i])
            print("f[{}] is {}".format(i, f[i]))
            print("g[{}] is {}".format(i, g[i]))

        return maxprofit

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
