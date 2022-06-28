class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for x in range(len(seats)):
            res+=abs(seats[x]-students[x])
        return res