class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        IsNegative = 1
        if dividend * divisor < 0:
            IsNegative = -1
            
        if divisor == 0:
            return 2**31-1
        if dividend == -2**31:
            if divisor == -1:
                return 2**31-1
            elif divisor == 1:
                return -2**31
            
        divd, divs = abs(dividend), abs(divisor)
        res = 0
        while divd >= divs:
            shift = 0
            while divd >= divs << shift:
                shift += 1
                
            res += 1 << (shift - 1)
            divd -= (divs << (shift-1))
        #end_while
        return IsNegative * res