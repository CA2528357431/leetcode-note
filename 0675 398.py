class Solution:

    def __init__(self, nums: List[int]):
        self.dic = {}
        for i in range(len(nums)):
            x = nums[i]
            if x not in self.dic:
                self.dic[x] = []
            self.dic[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dic[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)