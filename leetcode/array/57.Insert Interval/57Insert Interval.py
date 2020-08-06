class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda s: s[0])
        
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
                intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
            elif intervals[i][1] < intervals[i+1][0]:
                i += 1
            elif intervals[i][1] > intervals[i+1][1]:
                intervals.pop(i+1)
            # i += 1
                
        #end_while
        return intervals