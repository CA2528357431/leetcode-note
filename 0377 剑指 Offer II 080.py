class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        cur = []

        def deal(i):
            if i == n:
                if len(cur) == k:
                    res.append(cur.copy())
                return

            if len(cur) + (n - i) < k:
                return

            deal(i + 1)

            cur.append(i + 1)
            deal(i + 1)
            cur.pop()

        deal(0)

        return res