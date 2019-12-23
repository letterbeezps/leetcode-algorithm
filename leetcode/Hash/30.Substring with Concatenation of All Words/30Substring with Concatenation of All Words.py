# 单词可能会重复
# m, w = len(words), len(words[0])
# 最暴力的方法，取一个子串长度为m*w，子串里每个单词出现的次数和words里每个单词出现的次数一样
# 优化枚举方法，每次按照
# 0,w,2w,3w...
# 1,w+1,2w+1...
# w-1,2w-1  不然没有用上关键的条件，每个单词长度一样
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        n, m, w = len(s),len(words),len(words[0])
        #print(n,m,w)
        res = []
        Hash = collections.defaultdict(int)
        testdict = collections.defaultdict(int)
        for word in words:
            Hash[word] += 1
        for i in range(w):
            testdict.clear()
            sumn = 0
            l = i
            j = l
            while j+w<=n:
                #print(i)
                word = ''
                if j-m*w >= l:
                    word = s[j-m*w:j-m*w+w]
                    #print(word)
                    if testdict[word] == Hash[word]: sumn -= Hash[word]
                    testdict[word] -= 1
                    if testdict[word] == Hash[word]: sumn += Hash[word]
                word = s[j:j+w]
                if word not in Hash:  # 这个单词不在words里，该子串不用看了，新的起点重新计算
                    #print('sss'+word)
                    sumn = 0
                    testdict.clear()
                    l = j+w
                else:
                    if testdict[word] == Hash[word]: sumn -= Hash[word]
                    testdict[word] += 1
                    if testdict[word] == Hash[word]: sumn += Hash[word]
                #print(testdict)
                if sumn == m:
                    res.append(j-(m-1)*w)
                j+=w
        return res