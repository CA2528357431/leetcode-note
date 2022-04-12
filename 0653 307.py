class NumArray:

    def __init__(self, nums: List[int]):
        size = int(len(nums) ** 0.5)
        self.li = []
        cnt = 0
        for i in range(len(nums)):
            if i > 0 and i % size == 0:
                self.li.append(cnt)
                cnt = 0
            cnt += nums[i]
        self.li.append(cnt)
        self.nums = nums
        self.size = size

    def update(self, index: int, val: int) -> None:
        i = index // self.size
        delta = val - self.nums[index]
        self.nums[index] = val
        self.li[i] += delta

    def sumRange(self, left: int, right: int) -> int:
        ll = left // self.size
        rr = right // self.size
        if ll == rr:
            s = sum(self.nums[left:right + 1])
            return s

        s = 0
        lr = (ll + 1) * self.size - 1
        rl = rr * self.size
        s += sum(self.li[ll + 1:rr])
        s += sum(self.nums[left:lr + 1])
        s += sum(self.nums[rl:right + 1])
        return s