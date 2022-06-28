import random
class Solution:

    def __init__(self, nums: List[int]):
        self.ori = nums
        self.cur = nums.copy()

    def reset(self) -> List[int]:
        return self.ori

    def shuffle(self) -> List[int]:
        neo = self.ori.copy()

        for length in range(len(self.ori)):
            i = random.randint(0, len(self.ori) - 1 - length)
            self.cur[length] = neo[i]
            neo[i] = neo[len(self.ori) - 1 - length]

        return self.cur

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()