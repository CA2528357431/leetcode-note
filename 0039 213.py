class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        la = nums[1]
        cur1 = max(nums[1],nums[2])
        p = 2
        while p<=len(nums)-2:
            p+=1
            la,cur1 = cur1,max(cur1,la+nums[p])

        la = nums[0]
        cur2 = max(nums[1],nums[0])
        p = 1
        while p<=len(nums)-3:
            p+=1
            la,cur2 = cur2,max(cur2,la+nums[p])

        return max(cur1,cur2)

    # 分类讨论 不偷n-1,在[0 ,n-2] 和 不偷0,在[1,n-1]
    # 不偷n-1不代表一定偷0