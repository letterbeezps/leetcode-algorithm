class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 对于任何长度大于minsize符合条件的子串
        # 都可以从中构造一个长度未minsized的符合条件的子串
        n = len(s)
        ans = 0
        mp = collections.defaultdict(int)
        for i in range(n-minSize+1):
            mp[s[i:i+minSize]] += 1
            
        print(mp)
        
        for k, v in mp.items():
            if len(set(k)) <= maxLetters:
                ans = max(ans, v)
        return ans