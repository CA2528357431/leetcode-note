class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []

        def do(li, k):
            if k == 0:
                return [[]]

            if k == len(li):
                return [li]
            temp = li.copy()
            tail = li[-1]
            temp.pop()
            res1 = do(temp, k)
            res2 = do(temp, k - 1)
            for x in res2:
                x.append(tail)
            res1.extend(res2)
            return res1

        return do(list(range(1, n + 1)), k)

# 注意创建copy
# 为了res1、res2接受的数组一致

# k > n 则无解
# 所以 k<=li.length
# 要么 k-1 li-1，要么li - 1
# 所以两个弹出条件
# k == 0 和 li.length=k
