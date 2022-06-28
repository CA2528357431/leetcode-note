class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)