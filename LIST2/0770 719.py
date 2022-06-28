class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        # 寻找第k个？
        # 二分查找，分解出子问题：给定一个值，判断他是第几个

        nums.sort()
        n = len(nums)
        def find(de):
            l = 0
            cnt = 0
            for r in range(n):
                while nums[r]-nums[l]>de:
                    l+=1
                cnt += (r-l)
            return cnt
        le = 0
        ri = nums[-1]-nums[0]

        while le<ri:
            mid = (le+ri)//2
            res = find(mid)
            if res<k:
                le = mid+1
            else:
                ri = mid
        return le