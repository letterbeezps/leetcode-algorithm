'''
s = abc
t = ahbgdc
从头遍历两个字符串，再保持相对位置不变的情况下
找到s中每个字符在t中的存在性
若s是t的子序列，那么一定能遍历完整个s
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k, i = 0, 0  # k指向s，i指向t
        L_t, L_s = len(t), len(s)
        while i < L_t and k < L_s:  # 尽量把时间控制在l_s中
            if t[i] == s[k]:
                k += 1
            i += 1
        #end_while
        return k == L_s
        