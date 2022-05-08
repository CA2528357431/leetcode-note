# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get(li,cur):
            if not cur:
                return
            get(li,cur.left)
            li.append(cur.val)
            get(li,cur.right)
        li1 = []
        get(li1,root1)
        li2 = []
        get(li2,root2)
        res = [0]*(len(li1)+len(li2))
        i1 = 0
        i2 = 0
        i = 0
        while i1<len(li1) and i2<len(li2):
            if li1[i1]<li2[i2]:
                res[i] = li1[i1]
                i+=1
                i1+=1
            else:
                res[i] = li2[i2]
                i+=1
                i2+=1
        if i1==len(li1):
            while i2<len(li2):
                res[i] = li2[i2]
                i+=1
                i2+=1
        else:
            while i1<len(li1):
                res[i] = li1[i1]
                i+=1
                i1+=1
        return res





        return get(root1)