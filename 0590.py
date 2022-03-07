class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]
        for i in range(1,len(nums)):
            num=nums[i]
            while stack:
                x=stack[-1]
                g = gcd(x, num)
                if g == 1:
                    break
                stack.pop()
                num=num*x//g
            stack.append(num)
        return stack
