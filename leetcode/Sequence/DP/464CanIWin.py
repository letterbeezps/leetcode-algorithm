'''
由于给定的正整数小于max,因此我们可以用status表示当前的状态，最低位表示1是否被选取，0表示没有被选取，1表示被选取。
dfs的过程中，我们每次从可以选择的数中选择一个数，如果当前选择的数能够大于desire，那么就赢了。 如果我们当前选择了这个数，并且对手在剩下的状态中输了，那么我们也赢了。
'''
class Solution:
    def canIWin(self, maxn: int, desire: int) -> bool:
        status = 0
        if desire <= 1:
            return True
        if maxn * (maxn+1) < desire * 2:
            return False
        d = collections.defaultdict(bool)
        
        import copy
        dp = []
        for i in range(desire+1):
            dp.append(copy.deepcopy(d))
            
        def Caniwin(status: int, dp: list, maxn: int, desire: int) -> bool:
            if dp[desire].get(status):
                return True if dp[desire][status]==1 else False
            
            for i in range(maxn-1, -1, -1):
                if not (status & (1 << i)):
                    status |= (1<<i)
                    if i+1 >= desire or not Caniwin(status, dp, maxn, desire-i-1): # 此时status已经记录了第一次被选择的i
                        dp[desire][status] = 1  # means True
                        return True
                    #end_if
                    status ^= (1<<i)
            #end_for
            dp[desire][status] = 2  # means False
            return False
            
        return Caniwin(status, dp, maxn, desire)