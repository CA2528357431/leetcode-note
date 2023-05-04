class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def judge(x):
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True

        prime = [x for x in range(2, 1000) if judge(x)]

        def find(x):

            l = 0
            r = len(prime) - 1
            while l < r:
                mid = (l + r) // 2 + 1
                if prime[mid] < x:
                    l = mid
                elif prime[mid] >= x:
                    r = mid - 1

            return l

        pre = 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur - pre <= 0:
                return False
            elif cur - pre <= 2:
                pre = cur
                print(pre)
                continue
            mid = find(cur - pre)

            pre = cur - prime[mid]

        return True