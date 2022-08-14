class Solution:
    def reformat(self, s: str) -> str:
        nums = []
        alphas = []
        for c in s:
            if c.isdecimal():
                nums.append(c)
            else:
                alphas.append(c)
        if abs(len(alphas) - len(nums)) <= 1:

            if len(alphas) < len(nums):
                li = [nums[0]]
                i = 1
                for c in alphas:
                    li.append(c)
                    if i < len(nums):
                        li.append(nums[i])
                        i += 1
                return "".join(li)
            else:
                li = [alphas[0]]
                i = 1
                for c in nums:
                    li.append(c)
                    if i < len(alphas):
                        li.append(alphas[i])
                        i += 1
                return "".join(li)
        else:
            return ""
