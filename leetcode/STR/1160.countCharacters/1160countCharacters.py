class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            for c in word:
                if word.count(c) <= chars.count(c):
                    flag = 1
                    continue
                else:
                    flag = 0
                    break
            if flag:
                ans += len(word)
        return ans