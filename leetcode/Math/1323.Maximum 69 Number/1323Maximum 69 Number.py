class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        i = 0
        while i in range(len(str_num)):
            if str_num[i] == '6':
                break
            i += 1
        if i == len(str_num):
            return num
        ans = str_num[:i] + '9' + str_num[i+1:]
        return int(ans)
        
        