class Solution:
    def shortestCompletingWord(self, LP: str, words: List[str]) -> str:
        count = ''.join(filter(lambda x:x.isalpha(), LP)).lower()
        count = collections.Counter(count)
        # print(count)
        
        def matches(count, word):
            count_word = collections.Counter(word)
            for key in count:
                if key not in count_word:
                    return False
                elif count_word[key] < count[key]:
                    return False
            return True
        
        ans = ''
        min_l = 2**31
        for word in words:
            if min_l <= len(word):
                continue
            if not matches(count, word):
                continue
            min_l = len(word)
            ans = word
        return ans
    