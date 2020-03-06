class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def get_bin_number(x: int):
            count = 0
            
            while x:
                if x & 1:
                    count += 1
                x = x>>1
            return count
        temp = collections.defaultdict(list)
        for x in arr:
            count = get_bin_number(x)
            temp[count].append(x)
        ans = []
        max_count = max(temp.keys())
        for i in range(max_count+1):
            if temp.get(i):
                temp[i].sort()
                for x in temp[i]:
                    ans.append(x)
        return ans