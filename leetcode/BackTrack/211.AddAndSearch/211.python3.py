class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} 
        self.isword = '#'
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        
        for c in word:
            node = node.setdefault(c, {})
        node[self.isword] = 'Yes'
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchhelp(self.root, word, 0)
    
    def searchhelp(self, node, word, index) -> bool:
        #print(node)
        
        if index == len(word):
            return True if '#' in node else False
        c = word[index]
        
        if c != '.':
            node = node.get(c)
            if not node:
                return False
            return self.searchhelp(node, word, index+1)
        else:
            for k, newNode in node.items():
                if k != '#' and self.searchhelp(newNode, word, index+1):
                    return True
            return False
        
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)