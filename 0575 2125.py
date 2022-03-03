class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        cur = mass
        heapq.heapify(asteroids)
        while asteroids:
            if cur >= asteroids[0]:
                cur += heapq.heappop(asteroids)
            else:
                return False
        return True
