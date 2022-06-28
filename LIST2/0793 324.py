class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        li = nums.copy()
        li.sort()
        n = len(nums)
        s = 0
        b = n // 2
        if n % 2 == 1:
            b += 1
        s = b - 1
        b = n - 1

        # 为什么倒叙？
        # i i+half i-1

        # 如果正序？
        # i i+half i+1，有可能连续值

        for i in range(n):
            if i % 2 == 0:
                nums[i] = li[s]
                s -= 1

            else:
                nums[i] = li[b]
                b -= 1