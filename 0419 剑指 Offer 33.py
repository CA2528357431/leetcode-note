class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def judge(l,r):
            if l>=r:
                return True
            mid = r
            for i in range(l,r):
                if postorder[i]>=postorder[r]:
                    mid = i
                    break
            for i in range(mid+1,r):
                if postorder[i]<postorder[r]:
                    return False
            return judge(l,mid-1) and judge(mid,r-1)
        return judge(0,len(postorder)-1)
