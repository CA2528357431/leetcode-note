class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        '''
        return len(set(nums))!=len(nums)
        '''

        arc = set()
        for x in nums:
            if x in arc:
                return True
            else:
                arc.add(x)
        return False

