class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def judge(a, b):
            if a[0] > b[0] and a[1] > b[1]:
                return True
            else:
                return False

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        nums = [x[1] for x in envelopes]

        res = [nums[0]]
        for x in range(1, len(nums)):
            if nums[x] > res[-1]:
                res.append(nums[x])
            else:
                if nums[x] < res[0]:
                    res[0] = nums[x]
                else:
                    r = len(res) - 1
                    l = 0
                    while l < r:
                        mid = (l + r) // 2
                        if x == 3:
                            print(nums[x], res[mid], l, r)
                        if nums[x] > res[mid]:
                            l = mid + 1
                        else:
                            r = mid

                    res[l] = nums[x]

        return len(res)


