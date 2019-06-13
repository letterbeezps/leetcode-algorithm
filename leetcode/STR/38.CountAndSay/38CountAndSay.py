class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0:
            return ''
        res = '1'
        
        for i in range(n-1):
            pre = ''
            count = 0
            tmp = []
            for x in res:
                if x == pre or pre == '':
                    count += 1
                else:
                    tmp.append(count)
                    tmp.append(int(pre))
                    count = 1
                
                pre = x
            #end_for
            tmp.append(count)
            tmp.append(int(pre))
            res = ''.join(map(str, tmp))
        #end_for
        return res
                    