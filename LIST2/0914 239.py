class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        cur = deque()
        for i in range(len(nums)):
            while cur and cur[-1]<nums[i]:
                cur.pop()
            cur.append(nums[i])
            if i>=k and nums[i-k]==cur[0]:
                cur.popleft()
            # print(cur)
            if i>=k-1:
                res.append(cur[0])
        return res