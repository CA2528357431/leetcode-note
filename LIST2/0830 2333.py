from sortedcontainers import SortedDict


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)

        dic = SortedDict()
        for i in range(n):
            neo = abs(nums1[i] - nums2[i])
            if -neo not in dic:
                dic[-neo] = 0
            dic[-neo] += 1

        s = 0
        for key in dic:
            s += key * (-dic[key])
        if k >= s:
            return 0

        ks = list(dic.keys())
        for i in range(len(ks) - 1):
            cur = dic[ks[i]]
            delta = ks[i + 1] - ks[i]
            if delta * cur <= k:
                k -= delta * cur
                dic.pop(ks[i])
                dic[ks[i + 1]] += cur


            else:

                dic.pop(ks[i])
                a = k // cur
                b = k % cur

                k = 0

                t1 = b
                t2 = cur - b
                v1 = ks[i] + 1 + a
                v2 = ks[i] + a

                if v1 not in dic:
                    dic[v1] = 0
                dic[v1] += t1
                if v2 not in dic:
                    dic[v2] = 0
                dic[v2] += t2

                break

        if len(dic) == 1 and k != 0:

            v0 = ks[-1]
            t0 = dic[v0]

            dic.pop(v0)

            a = k // t0
            b = k % t0

            t1 = b
            t2 = t0 - b
            v1 = v0 + 1 + a
            v2 = v0 + a

            if v1 not in dic:
                dic[v1] = 0
            dic[v1] += t1
            if v2 not in dic:
                dic[v2] = 0
            dic[v2] += t2

        res = 0

        for k, v in dic.items():
            res += v * (k ** 2)

        return res