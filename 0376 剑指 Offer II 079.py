class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []

        def deal(i):
            if i == len(nums):
                res.append(cur.copy())
                return

            deal(i + 1)

            cur.append(nums[i])
            deal(i + 1)
            cur.pop()

        deal(0)

        return res