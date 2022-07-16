class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        j = 0
        cur = 0
        index = -1

        cap = 0
        jj = -1

        for i in range(len(passengers)):

            while j < len(buses) and passengers[i] > buses[j]:
                j += 1
                cur = 0
            if j == len(buses):
                break

            cur += 1

            cap = cur
            jj = j
            index = i

            if cur == capacity:
                cur = 0
                j += 1

        if jj != len(buses) - 1:
            return buses[-1]

        if cap != capacity and passengers[index] < buses[jj]:
            return buses[jj]
        for i in range(index, -1, -1):
            if i == 0:
                return passengers[0] - 1
            if passengers[i] - 1 != passengers[i - 1]:
                return passengers[i] - 1
