'''
首先，先确定这一行最多能放几个单词
1 最后一行：只要左对齐
2 如果这一行只有一个单词：在行尾补上空格
3 其他情况：计算空格数，均匀分布
'''
class Solution:
    
    def space(self, x: int) -> str:
        res = ''
        while x:
            res += ' '
            x -= 1
        return res
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            j = i+1
            s = len(words[i])  # 'this is an'
            rs = len(words[i]) # 'thisisan'
            while j < len(words) and s+1+len(words[j]) <= maxWidth:
                s += len(words[j]) + 1
                rs += len(words[j])
                j += 1
            rs = maxWidth - rs
            line = words[i]
            if j == len(words):
                for k in range(i+1, j):
                    line += ' ' + words[k]
                line += self.space(maxWidth - len(line))
                
            elif j - i == 1:
                line += self.space(maxWidth - len(line))
                
            else:
                base = rs // (j-i-1)  #如果有三个单词，那么这一行就有两处    空格，所以减一
                rem = rs % (j-i-1)
                i += 1
                k = 0
                while i < j:
                    line += self.space(base + (k < rem)) + words[i]
                    k += 1
                    i += 1
            i = j
            res.append(line)
        return res