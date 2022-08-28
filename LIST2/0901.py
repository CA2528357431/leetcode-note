class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        def do(x):
            res = 0
            cur = 0
            for n in nums:
                if cur+n>x:
                    return res
                res+=1
                cur+=n
            return res
        res = [do(x) for x in queries]
        return res