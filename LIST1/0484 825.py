class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        i = 0
        while i < n and ages[i] <= 14:
            i += 1

        x = i
        y = 0
        res = 0
        while x < n:
            mul = 1
            while x + 1 < n and ages[x + 1] == ages[x]:
                x += 1
                mul += 1
            while y < x and ages[y] <= 0.5 * ages[x] + 7:
                y += 1
            res += (x - y) * mul
            x += 1

        return res