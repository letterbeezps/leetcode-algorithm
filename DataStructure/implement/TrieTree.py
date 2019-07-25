class Node:

    def __init__(self, isword=False):
        self._isword = isword
        self._next = {}  # chars: Node

class Trie:

    def __init__(self):
        self._root = Node()
        self._size = 0

    def add(self, word: str):

        current = self._root
        for s in word: 
            node = current._next.get(s)

            if not node:
                current._next[s] = Node()

            current = current._next.get(s)

        if not current._isword:
            self._size += 1
            current._isword = True

    def contains(self, word: str) -> bool:
        current = self._root

        for c in word:
            node = current._next.get(c)
            if not node:
                return False
            current = node
        
        return current._isword

    def containsPrefix(self, word: str) -> bool:
        current = self._root

        for c in word:
            node = current._next.get(c)
            if not node:
                return False
            current = node
        
        return True   

    '''
    1 被删除单词是另一个单词的前缀，只把该word的最后一个节点的isword改为False
    2 如果单词的所有字母都没有分之，直接删除整个分之
    3 如果删除了单词最后一个字母，其他的字母有多个分之
    '''
    def remove(self, word: str) -> bool:
        multiChildNode = None 
        multiChildNodeIndex = -1

        current = self._root

        for i, c in enumerate(word):
            child = current._next.get(c)

            if not child:
                return False

            if not child._next:
                multiChildNode = child
                multiChildNodeIndex = i
            
            current = child

        if current._next:
            if current._isword:
                current._isword = False
                self._size -= 1 
                return True

            return False # this wprd is only Prefix 

        if multiChildNodeIndex == -1: 
            del self._root._next[word[0]]  # this means is only a lonly branch
            self._size -= 1
            return True

        if multiChildNodeIndex != len(word)-1:
            del multiChildNode._next[word[multiChildNodeIndex+1]]
            self._size -= 1 
            return True    

        return False