class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def do(l, r):
            if l >= r:
                return

            randi = randint(l, r)
            nums[l], nums[randi] = nums[randi], nums[l]

            st = nums[l]
            li = l
            ri = r
            while li < ri:
                while ri > li and nums[ri] >= st:
                    ri -= 1
                if ri == li:
                    break
                nums[li] = nums[ri]
                li += 1
                while li < ri and nums[li] <= st:
                    li += 1
                if li == ri:
                    break
                nums[ri] = nums[li]
                ri -= 1

            nums[li] = st
            do(l, li - 1)
            do(li + 1, r)

        do(0, len(nums) - 1)
        return nums