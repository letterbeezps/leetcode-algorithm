# 如果要判断一个给定的序列是不是二叉树的后序遍历（左右中），把它变成（中右左），再用前序的判别方法。
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        pre=preorder.split(',')
        if pre[-1]!='#': return False
        
        stack=0
        for i in pre[:-1]:
            if i!='#': stack+=1
            elif stack>0: stack-=1
            else: return False
            
        if stack==0: return True
        return False