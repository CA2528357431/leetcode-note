class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = 0
        far = cur + nums[cur]
        step = 0
        while cur < far and far < len(nums) - 1:
            cur += 1
            far = max(far, cur + nums[cur])
            if cur == far:
                step+=1

        if far >= len(nums) - 1:
            return True
        return False

    # 不断获得最远距离far
    # far之前的元素都可达
    # 当far>=n-1可达终点
    # 如果cur>=far，证明无法前进
