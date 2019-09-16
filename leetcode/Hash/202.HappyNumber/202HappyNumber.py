class Solution:
    
    def sum_of_square(self, n: int) -> int:
        if n < 10: 
            return n**2
        return self.sum_of_square(n // 10) + (n % 10)**2
    
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 4:
            return False
        return self.isHappy(self.sum_of_square(n))
        

#####solutio 2##########
class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        sumn, dumn = 0, n
        while sumn != 1:
            sumn = 0
            while dumn:
                sumn += (dumn%10) ** 2
                dumn //= 10
            if sumn in set1:
                return False
            set1.add(sumn)
            dumn = sumn
        
        return True