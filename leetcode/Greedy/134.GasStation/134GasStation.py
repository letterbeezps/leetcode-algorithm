class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        n = len(gas)
        while i < n:
            j = 0
            gas_left = 0
            while j < n:
                k = (i+j) % n
                gas_left += gas[k] - cost[k]
                if gas_left < 0:
                    break;
                j += 1
            if j >= n:
                return i
            i += j+1
        #end_while
        return -1