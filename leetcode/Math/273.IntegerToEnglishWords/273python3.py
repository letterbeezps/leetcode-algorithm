class Solution:
    def numberToWords(self, num: int) -> str:
        self.hundred = 100
        self.thousand = 1000
        self.million = 1000000
        self.billion = 1000000000
        self.numbers = collections.defaultdict(str)
        self.numbers[self.hundred] = 'Hundred'
        self.numbers[self.thousand] = 'Thousand'
        self.numbers[self.million] = 'Million'
        self.numbers[self.billion] = 'Billion'
        
        number20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
                    'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                    'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
                    'Seventeen', 'Eighteen', 'Nineteen']
        number2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
                   'Seventy', 'Eighty', 'Ninety']
        
        for i in range(20):
            self.numbers[i] = number20[i]
        for i in range(20, 100, 10):
            self.numbers[i] = number2[i//10-2]
        res = ''
        
        k = 1000000000
        while k >= 100:
            if num >= k:
                res += ' ' + self.get3(num//k) + ' ' + self.numbers[k]
                num %= k
            k //= 1000
        if num:
            res += ' ' + self.get3(num)
        if not res:
            res += ' ' + self.numbers[0]
        return res[1:]
        
    def get3(self, num: int) -> str:
        res = ''
        if num >= self.hundred:
            res +=' ' + self.numbers[num // self.hundred] + ' ' + self.numbers[self.hundred]
            num %= self.hundred
        if num:
            if num < 20:
                res += ' ' + self.numbers[num]
            elif num % 10 == 0:
                res += ' ' + self.numbers[num]
            else:
                res += ' ' + self.numbers[num//10 * 10] + ' ' + self.numbers[num%10]
        return res[1:]
        
        