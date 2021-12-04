# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        li = [root]
        res = []
        while li:
            neo = []
            for node in li:
                if not node:
                    res.append("null")
                else:
                    res.append(str(node.val))
                    neo.append(node.left)
                    neo.append(node.right)
            li = neo
        while res[-1] == "null":
            res.pop()
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        nums = []
        for x in data[1:-1].split(","):

            if x != "null":
                nums.append(int(x))
            else:
                nums.append(None)
        count = 0
        root = TreeNode(nums[0])
        cur = [root]
        neo = []
        for i in range(1, len(nums)):
            if nums[i] is not None:
                node = TreeNode(nums[i])
                neo.append(node)

                r = cur[count // 2]
                if count % 2 == 0:
                    r.left = node
                else:
                    r.right = node
            count += 1
            if count == len(cur) * 2:
                cur = neo
                neo = []
                count = 0
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))