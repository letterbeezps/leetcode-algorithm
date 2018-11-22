class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    # Create a binary tree from a list
    def add(self, itemlist):
        if len(itemlist) == 0: # list is none
            self.root = None
            return
        self.root = Node(itemlist[0])
        q = [self.root] # list of node
        front = 0
        index = 1
        while index < len(itemlist):
            pop_node = q[front]
            front = front + 1
            item = itemlist[index]
            index = index + 1
            if item:
                pop_node.left = Node(item)
                q.append(pop_node.left)
            
            if index >= len(itemlist):
                break

            # if last item is none, search the next item and add it to right_tree
            item = itemlist[index]
            index = index + 1
            if item:
                pop_node.right = Node(item)
                q.append(pop_node.right)

    def preorder(self, root):  # preorder
        if root is None:
            return [None]
        result = [root.item]
        left_item = self.preorder(root.left)
        right_item = self.preorder(root.right)
        return result + left_item + right_item


t = Tree()
test = [1, None, 3, 4, 5, 6]
t.add(test)

print(t.preorder(t.root))
