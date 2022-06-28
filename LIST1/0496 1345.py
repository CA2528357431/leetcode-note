class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        used = [False] * n
        used[0] = True

        dic = {}
        for i in range(n):
            if arr[i] not in dic:
                dic[arr[i]] = []

            if i in (0, n - 1):
                dic[arr[i]].append(i)
            elif arr[i] != arr[i - 1] or arr[i] != arr[i + 1]:
                dic[arr[i]].append(i)
                # 连续一致的数字只存开头结尾

        def find(cur):
            now = 0

            while True:
                nxt = []
                for c in cur:
                    if c == n - 1:
                        return now
                    if c - 1 >= 0 and not used[c - 1]:
                        if c - 1 == n - 1:
                            return now + 1

                        used[c - 1] = True
                        nxt.append(c - 1)
                    if c + 1 < n and not used[c + 1]:
                        if c + 1 == n - 1:
                            return now + 1

                        used[c + 1] = True
                        nxt.append(c + 1)
                    for i in dic[arr[c]]:
                        if i == n - 1:
                            return now + 1
                        if not used[i]:
                            used[i] = True
                            nxt.append(i)
                    dic[arr[c]] = []
                    # 防止cur内不同的i对应一样的值，形成重复访问

                cur = nxt
                now += 1

        return find([0])