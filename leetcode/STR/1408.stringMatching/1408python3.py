class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            for s in words:
                if s == word:
                    continue
                if word in s:
                    ans.append(word)
                    break
        return ans