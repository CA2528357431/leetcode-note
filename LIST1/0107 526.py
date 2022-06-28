class Solution:
    def countArrangement(self, n):

        used = set()

        def add(cur):
            if cur == n + 1:
                return 1

            else:
                total = 0
                for x in range(1, n + 1):
                    if x not in used and (x % cur == 0 or cur % x == 0):
                        used.add(x)
                        total += add(cur + 1)
                        used.remove(x)
                return total

        a = add(1)
        return a


sol = Solution()
sol.countArrangement(15)
