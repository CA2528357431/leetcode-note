# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, val: int) -> int:
        cur = [self.root]

        while cur:
            nxt = []
            for n in cur:
                if n.left and n.right:
                    nxt.append(n.left)
                    nxt.append(n.right)
                elif not n.left:
                    n.left = TreeNode(val)
                    return n.val
                else:
                    n.right = TreeNode(val)
                    return n.val
            cur = nxt

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()