class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        dsum = sum(nums) - sum(set(nums))
        dn = len(nums) - len(set(nums))

        return dsum // dn
        '''

        # 快慢针
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow

    # num[a]=b 视为(a,b)向量
    # 为何必然成环？
    # 全链只有0一个入口，而有一个点（重复点）有多个入口\

    # 背下来 相遇点、初点到重复点距离一样