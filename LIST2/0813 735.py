class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for n in asteroids:
            while True:
                if not res:
                    res.append(n)
                    break
                if res[-1] * n > 0:
                    res.append(n)
                    break
                if res[-1] < 0 and n > 0:
                    res.append(n)
                    break

                if abs(res[-1]) == abs(n):
                    res.pop()
                    break
                elif abs(res[-1]) < abs(n):
                    res.pop()
                else:
                    break
        return res
