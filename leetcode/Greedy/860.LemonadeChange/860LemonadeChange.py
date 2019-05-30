class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives:  # 有五元零钱，找零
                    fives -= 1
                    tens += 1
                else:
                    return False  # 没有返回F
            else:
                t = 15    # 收到20，要找零15
                if tens:  # 有10元零钱，先看看有没有10元零钱
                    t -= 10
                    tens -= 1
                while t and fives:
                    t -= 5
                    fives -= 1
                if t:     # 无法完成找零
                    return False
        #end_for
        return True