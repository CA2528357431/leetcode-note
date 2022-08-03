class Solution:
    def maximumGroups(self, grades: List[int]) -> int:

        def do(x):
            return (1+x)*x//2

        n = len(grades)
        l = 1
        r = n
        while l<r:
            mid = (l+r)//2+1
            x = do(mid)
            if x<n:
                l = mid
            elif x>n:
                r = mid-1
            else:
                return mid
        return l