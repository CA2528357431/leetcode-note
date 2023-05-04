class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        acc = nums.copy()
        n = len(nums)
        for i in range(1, n):
            acc[i] += acc[i - 1]

        def find(q):
            l = 0
            r = n - 1
            while l < r:
                mid = (l + r) // 2 + 1
                if nums[mid] < q:
                    l = mid
                else:
                    r = mid - 1
            return l

        def do(q):
            if q >= nums[-1] or q <= nums[0]:
                return abs(acc[-1] - n * q)
            index = find(q)
            # print(index)
            pre = abs(acc[index] - (index + 1) * q)
            post = abs((acc[-1] - acc[index]) - (n - index - 1) * q)
            # print(pre,post,index)
            return pre + post

        return [do(q) for q in queries]