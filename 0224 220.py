class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:


        # 桶排序

        if k == 0:
            return False

        dic = {}
        for i in range(len(nums)):
            ind = nums[i] // (t + 1)

            if ind in dic:
                return True
            if ind + 1 in dic:
                if dic[ind + 1] - nums[i] <= t:
                    return True
            if ind - 1 in dic:
                if -dic[ind - 1] + nums[i] <= t:
                    return True
            dic[ind] = nums[i]
            if i >= k:
                dic.pop(nums[i - k] // (t + 1))
        return False