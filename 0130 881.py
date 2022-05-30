class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n == 1:
            return 1

        people.sort()
        if people[0] + people[1] > limit:
            return n

        res = 0

        l = 0
        r = n - 1
        while people[l] + people[r] > limit:
            r -= 1
        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1
            else:
                r -= 1
        return res + (n - 2 * res)
