class SegmentTreeNode:
    def __init__(self, start, end, val, left=None, right=None):
        self.start =start
        self.end = end
        self.val = val  # val的值根据问题本身来定义
        self.mid = start + end >> 1
        self.left = left
        self.right = right

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._buildTree(0, len(self.nums)-1)

    def rangeQuery(self, i, j):
        return  self._rangeQuery(self.root, i, j)
    
    def update(self, i, val):
        self._update(self.root, i, val)

    def _buildTree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])  # 叶子结点就是数组的某一个元素
        mid = start + end >> 1
        left = self._buildTree(start, mid)
        right = self._buildTree(mid+1, end)

        return SegmentTreeNode(start, end, left.val+right.val, left, right)
    
    def _update(self, root: SegmentTreeNode, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        mid = root.start + root.end >> 1
        if i <= mid:
            self._update(root.left, i, val)
        else:
            self._update(root.right, i, val)
        root.val = root.left.val + root.right.val

    def _rangeQuery(self, root: SegmentTreeNode, i, j):
        if root.start == i and root.end == j:
            return root.val
        if j <= root.mid:
            return self._rangeQuery(root.left, i, j)
        elif i > root.mid:
            return self._rangeQuery(root.right, i, j)
        else:
            return self._rangeQuery(root.left, i, root.mid) + self._rangeQuery(root.right, root.mid+1, j)
