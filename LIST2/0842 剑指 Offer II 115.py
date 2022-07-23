class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        mto = {i: 0 for i in range(1, n + 1)}
        mfrom = {i: [] for i in range(1, n + 1)}

        for li in sequences:
            for i in range(len(li) - 1):
                s = li[i]
                e = li[i + 1]
                mto[e] += 1
                mfrom[s].append(e)

        ind = -1
        pre = ind
        judge = False
        for i in mto:
            l = mto[i]
            if l == 0:
                if ind != pre:
                    return False
                ind = i
        if ind == pre:
            return False

        for x in nums:

            if x != ind:
                return False

            pre = ind
            for i in mfrom[ind]:
                mto[i] -= 1
                if mto[i] == 0:
                    if ind != pre:
                        return False
                    ind = i

        return True







