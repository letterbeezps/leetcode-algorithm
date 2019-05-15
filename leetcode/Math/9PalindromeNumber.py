class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        尽量不要把整数转为字符串来解决
        '''
        if x < 0:
            return False
        div, num = 1, x
        while num // div >= 10:
            div *= 10

        while num != 0:
            left = num // div
            right = num % 10
            if left != right:
                return False
            num = (num-left*div) // 10
            div //= 100
        #end_while
        return True