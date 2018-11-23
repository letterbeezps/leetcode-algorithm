from BinaryTree import Tree

def zp_dfs(u, sum):
    sum -= u.item  # means we have reach node u
    if sum == 0 and u.left == None and u.right == None:  # if node u is leave_node and subSum is 0
        return True

    # reach node u, next to check U_child
    # regard u_child as new root
    elif u.left and zp_dfs(u.left, sum): return True
    elif u.right and zp_dfs(u.right, sum): return True
    else:
        return False

def hasPathSum(root, sum):
    if root == None: # no path
        return False
    else:
        return zp_dfs(root, sum)

sum = 22
q = Tree()
test1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
q.add(test1)
print(q.preorder(q.root))
q_node = q.root
if hasPathSum(q_node, sum):
    print('True')
else:
    print('False')