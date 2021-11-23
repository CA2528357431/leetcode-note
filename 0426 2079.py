class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cur = capacity
        steps = 0
        for i in range(len(plants)):
            if cur>=plants[i]:
                cur-=plants[i]
                steps+=1
            else:
                steps+=(2*i+1)
                cur = capacity-plants[i]
        return steps