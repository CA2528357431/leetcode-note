class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        # 局部迭代
        # 而不是对整个数组进行多次合并
        # 反例  [2,4,8,3,6,9]-->[4,8,6,9]
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
