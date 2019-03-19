# -*- coding: utf-8 -*-
# 求最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        preS = self.preHandleString(s)  # 先预处理字符串
        ls = len(preS)  # 处理后字符串的长度
        rightSide = 0  # 右边界
        rightSideCenter = 0  # 右边界对应的回文中心

        # 以每个字符为中心的回文长度的一半
        halfLenArr = [0 for i in range(ls)] 

        center = 0  # 记录回文中心
        longesHalf = 0  # 最长的回文长度

        for i in range(ls):
            needCalc = True  # 代表中心需要拓展
            if (rightSide > i):  # 如果在右边界的覆盖范围内
                leftCenter = 2 * rightSideCenter - i
                halfLenArr[i] = halfLenArr[leftCenter]  # 这是根据回文性质得到的结论

                if (i+halfLenArr[i] > rightSide):  # 如果超过了右边界，则需要调整
                    halfLenArr[i] = rightSide - i  # 在边界范围内的值肯定是回文的

                if (i+halfLenArr[leftCenter] < rightSide):
                    needCalc = False

            # 中心拓展部分
            if needCalc:
                while(i-1-halfLenArr[i] >= 0 and i+1+halfLenArr[i] < ls):
                    if preS[i-1-halfLenArr[i]] == preS[i+1+halfLenArr[i]]:
                        halfLenArr[i] += 1
                    else:
                        break
                    
                    # 更新右边界和中心
                    rightSideCenter = i
                    rightSide = i + halfLenArr[i]
                    # 记录最长回文串和其中心
                    if halfLenArr[i] > longesHalf:
                        center = i
                        longesHalf = halfLenArr[i]
        # endfor
        # 取出最长回文字符串
        lastS = ''
        start_L = center - longesHalf + 1
        end_L = center + longesHalf
        for i in range(start_L, end_L+1)[::2]:
            lastS += preS[i]

        return lastS




    # 预处理字符串，给每个字符之间添加 '#'
    def preHandleString(self, s: str) -> str:
        ls = len(s)
        preS = ''
        preS += '#'
        for i in range(ls):
            preS += s[i]
            preS += '#'
        
        return preS


def stringToString(input):
    return input[1:-1]

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
            s = stringToString(line)

            # for test
            # Solution().longestPalindrome(s)
            
            
            ret = Solution().longestPalindrome(s)

            out = (ret)
            print(out)
            
        except StopIteration:
            break

if __name__ == '__main__':
    main()