class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        对于单调不递减的序列，删除后k位就行了
        对于有逆序列的情况如 12342， 这时候就删除2前面的4 和 3
        '''
        res = ''
        for x in num:
            while len(res) and res[-1] > x and k:
                res = res[:-1]  # 删除res当前的末位
                k -= 1
            #end_while
            res += x
        if k: 
            res = res[:-k]
        i = 0
        while i < len(res)-1 and res[i] == '0':
            i += 1
            
        if i == len(res): 
            return '0'
        else:
            return res[i:]