class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.isword = '#'
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.isword] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        
        for c in word:
            node = node.get(c)
            if not node:
                return False
        return True if '#' in node else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        
        for c in prefix:
            node = node.get(c)
            if not node:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)