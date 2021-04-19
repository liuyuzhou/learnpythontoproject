class SearchTree(object):
    def __init__(self, small, large):
        self.small = small
        self.large = large

    def valid_bst(self, root, small, large):
        """
        :param root:
        :param small:
        :param large:
        :return:
        """
        if root is None:
            return True
        if self.small >= root.val or self.large <= root.val:
            return False
        return self.valid_bst(root.left, self.small, root.val) and self.valid_bst(root.right, root.val, self.large)

    def is_valid_bst(self, root):
        """
        :param root:
        :return:
        """
        return self.valid_bst(root, self.small, self.large)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode(12)
b = TreeNode(5)
c = TreeNode(18)
d = TreeNode(2)
e = TreeNode(9)
f = TreeNode(15)
g = TreeNode(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
m = SearchTree(d.val, g.val)
print(f'该树是否是二叉搜索树：{m.is_valid_bst(a)}')
print(f'该树是否是二叉搜索树：{m.is_valid_bst(f)}')
