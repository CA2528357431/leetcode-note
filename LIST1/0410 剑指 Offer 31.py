class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        cur = []
        n = len(pushed)
        i = 0
        j = 0
        while i<n:
            cur.append(pushed[i])
            i+=1
            while len(cur)>0 and cur[-1]==popped[j]:
                cur.pop()
                j+=1
        return j==n