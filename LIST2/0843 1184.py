class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        n = len(distance)

        a = 0

        if destination < start:
            destination += n

        for i in range(start, destination):
            i = i % n
            a += distance[i]

        return min(a, total - a)