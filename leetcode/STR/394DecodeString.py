class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
            else:  # 当前数是数字
                k = 0
                while s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                sum = 1  # 数字后面第一个字符是"["，寻找与之对应的"]"
                j = i + 1
                while sum > 0:
                    if s[j] == '[':
                        sum += 1
                    if s[j] == ']':
                        sum -= 1
                    j += 1  # 此时j指向符合条件的"]"的后一位
                    
                sub_s = self.decodeString(s[i+1: j-1])
                while k > 0:
                    res += sub_s
                    k -= 1
                i = j
        return res