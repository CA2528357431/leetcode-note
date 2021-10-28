class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        '''
        li = [int(x) for x in str(n)]
        li.sort()

        res = False

        def dfs(i, cur):
            if i == len(li):

                if (cur & (cur - 1)) == 0:
                    nonlocal res
                    res = True
                return

            for x in range(i, len(li)):
                if x > i and li[x] == li[x - 1]:
                    continue
                if i == 0 and li[x] == 0:
                    continue

                li[x], li[i] = li[i], li[x]
                dfs(i + 1, cur * 10 + li[i])
                li[x], li[i] = li[i], li[x]

        dfs(0, 0)
        return res
        '''



        check = []

        def deal(x):
            string = str(x)
            dic = {}
            for c in string:
                dic[c] = dic.get(c, 0) + 1
            return dic

        bit = 1
        for i in range(31):
            check.append(deal(bit))
            bit *= 2

        neo = deal(n)

        return neo in check