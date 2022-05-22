# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        li = []

        def do(cur):
            if not cur:
                li.append("N")
                return
            else:
                li.append(str(cur.val))
                do(cur.left)
                do(cur.right)

        do(root)
        string = ",".join(li)
        return string

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        if data == "N":
            return None

        li = data.split(",")
        root = TreeNode(int(li[0]))

        i = 0

        def do():
            nonlocal i
            if li[i] == "N":
                i += 1
                return None
            node = TreeNode(int(li[i]))
            i += 1
            l = do()
            r = do()
            node.left = l
            node.right = r
            return node

        return do()

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans