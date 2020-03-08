class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        
        while l<r:
            mid = l+r >> 1
            if letters[mid] <= target:
                l = mid+1
            else:
                r = mid
                
        return letters[l] if letters[l]>target else letters[0]