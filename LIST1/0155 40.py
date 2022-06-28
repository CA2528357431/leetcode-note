class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()

        def do(path, l, tar):
            if tar == 0:
                res.append(path.copy())

            for i in range(l, len(candidates)):

                # 利用排序减小范围
                if candidates[i] > tar:
                    break

                # 很重点
                if i > l and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                do(path, i + 1, tar - candidates[i])
                path.pop()

        do(path, 0, target)
        return res