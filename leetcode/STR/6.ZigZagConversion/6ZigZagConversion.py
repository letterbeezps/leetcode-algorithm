'''
字符填充 PAYPALISHIRING
0   p
1   a       x
2   y       x
|   |       x
n-1 s[n-1]
向上填充时，收尾两个字符串不再接受新字符
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        sc = [''] * numRows
        
        i = 0
        while i < l:
            for idx in range(numRows):
                if i < l:
                    sc[idx] += s[i]
                    i += 1
            for idx in range(numRows-2, 0, -1):
                if i < l:
                    sc[idx] += s[i]
                    i += 1
        print(sc)
        s = ''.join(sc)
        return s