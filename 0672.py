class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        def finds(li, tar):
            if li[-1] < tar:
                return -1
            if li[0] >= tar:
                return 0
            n = len(li)
            l = 0
            r = n - 1
            while l < r:
                mid = (l + r) // 2
                if li[mid] < tar:
                    l = mid + 1
                else:
                    r = mid
            return l

        def finde(li, tar):
            if li[-1] <= tar:
                return -1
            if li[0] > tar:
                return 0
            n = len(li)
            l = 0
            r = n - 1
            while l < r:
                mid = (l + r) // 2
                if li[mid] <= tar:
                    l = mid + 1
                else:
                    r = mid
            return l

        pp = persons.copy()
        pp.sort()
        li = [0] * len(persons)
        for s, e in flowers:
            ss = finds(pp, s)
            ee = finde(pp, e)
            if ss < 0:
                continue
            li[ss] += 1
            if ee >= 0:
                li[ee] -= 1

        cnt = [0] * len(persons)
        cnt[0] = li[0]
        for i in range(1, len(persons)):
            cnt[i] = cnt[i - 1] + li[i]

        dic = {pp[i]: cnt[i] for i in range(len(persons))}
        ans = [0] * len(persons)
        for x in range(len(persons)):
            ans[x] = dic[persons[x]]
        return ans