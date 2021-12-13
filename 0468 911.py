class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        tops = [-1] * (len(persons))
        vote = {}
        cur = -1
        for i in range(len(persons)):

            p = persons[i]
            if p not in vote:
                vote[p] = 0
            vote[p] += 1
            if cur == -1 or vote[p] >= vote[cur]:
                cur = p
            tops[i] = cur
            # >=是因为同票时新票优先
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if self.times[mid] <= t:
                l = mid
            else:
                r = mid - 1
        # times[r]符合条件
        # 因此结果是tops[r]
        return self.tops[l]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)