from BinaryTree import Tree

p = Tree()
q = Tree()
test1 = [1, None,2]
test2 = [1, 2]
p.add(test1)
q.add(test2)

p_node = p.root
q_node = q.root

def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.item == q.item:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
    
if isSameTree(p_node, q_node):
    print('True')
else:
    print('False')