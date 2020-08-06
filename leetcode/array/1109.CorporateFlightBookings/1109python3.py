class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        tag = [0] * 20003
        
        for booking in bookings:
            tag[booking[0]] += booking[2]
            tag[booking[1]+1] -= booking[2]
        for i in range(n):
            if not i:
                res[i] = tag[i+1]
            else:
                res[i] = res[i-1] + tag[i+1]
        return res