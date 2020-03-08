class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: [-len(x),x])
        
        dic = set(words)
        
        for word in words:
            prefix = ''
            valid = True
            
            for i in range(len(word)-1):
                if not valid:
                    break
                prefix += word[i]
                if prefix not in dic:
                    valid = False
            if valid:
                return word
        return ''