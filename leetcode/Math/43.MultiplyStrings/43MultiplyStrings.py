'''
max_len = len(num1) + len(num2)
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not len(num1) or not len(num2):
            return '0'
        max_len = len(num1) + len(num2)
        res = [0] * max_len
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                Pos_low = i+j+1
                Pos_high = i+j
                mul += res[Pos_low]  # 加上之前的计算结果
                res[Pos_low] = mul%10
                res[Pos_high] += mul//10
        res = list(map(str, res))
        str_res = ''.join(res).lstrip('0')
        return str_res if len(str_res) else '0'