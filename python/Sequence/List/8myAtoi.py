class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        num = 0 
        sign = 1
        len_str = len(str)
        if len_str == 0:  # 输入为空，返回0
            return 0
        i = 0

        while str[i] == ' ':  # 先跳过前面的空格
            i = i + 1
            if i == len_str:  # 输入全为空格，返回0
                return 0

        if str[i] == '+':
            i = i + 1
        elif str[i] == '-':
            sign = -1
            i = i + 1

        while i < len_str:
            if str[i] < '0' or str[i] > '9':  # 碰到第一个非数字的字符，结束
                break
            if num > INT_MAX // 10:  # 判断是否溢出
                if sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX
            elif num == INT_MAX // 10 and int(str[i]) > INT_MAX % 10:
                if sign == -1:
                    return INT_MIN
                else:
                    return INT_MAX

            num = num * 10 + int(str[i])
            i = i + 1
            
        return num * sign