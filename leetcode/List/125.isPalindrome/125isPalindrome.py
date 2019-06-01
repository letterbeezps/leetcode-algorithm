class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        使用filter和str.isalnum参数获得s中的字母和数字，返回一个迭代器
        .join函数将其拼接
        最后变成小写
        然后使用切片运算符
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]