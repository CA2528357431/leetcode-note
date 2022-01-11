class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        m = {}
        n = len(nums)
        res = 0


        for c in range(n - 2, 1, -1):
            for d in range(c + 1, n):
                do = nums[d] - nums[c]
                if do not in m:
                    m[do] = 0
                m[do] += 1
            # 此时统计了 c.cur 之后的所有差

            b = c - 1
            # 固定b
            # a和b.other尽管也有可能在统计表中，但如果此时就算，那就丢失了c在[b.other,c.cur]中间的解
            # 因此，任何一个(a,b)对都应当在c=b+1时再统计
            for a in range(b):
                do = nums[a] + nums[b]
                if do in m:
                    res += m[do]
        return res