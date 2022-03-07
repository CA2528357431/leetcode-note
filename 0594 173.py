# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cur = -1

        def get(node):
            if not node:
                return []
            return get(node.left) + [node.val] + get(node.right)

        self.li = get(root)

    def next(self) -> int:
        self.cur += 1
        return self.li[self.cur]

    def hasNext(self) -> bool:
        return self.cur < len(self.li) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()