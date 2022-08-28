class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        mineng = 0
        minexp = 0
        tenergy = sum(energy)+1
        if tenergy>initialEnergy:
            mineng = tenergy-initialEnergy
        for x in experience:
            minexp = max(minexp,x-initialExperience+1)
            initialExperience+=x
        return mineng+minexp