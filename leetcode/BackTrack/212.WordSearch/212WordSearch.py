# trie tree
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False
        
class TrieTree:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        
        res = []
        trie = TrieTree()
        node = trie.root
        for word in words:
            trie.insert(word)
            
        direcs = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def dfs(node: Node, path, i, j, res):
            if node.isWord:
                res.append(path[:])
                node.isWord = False
            if i<0 or i>=m or j<0 or j>=n:
                return
            tmp = board[i][j]
            node = node.children.get(tmp, None)
            if not node:
                return

            board[i][j] = '#'
            for dx, dy in direcs:
                dfs(node, path+tmp, i+dx, j+dy,  res)
            board[i][j] = tmp
        
        for i in range(m):
            for j in range(n):
                dfs(node, '', i, j, res)
        return res
                