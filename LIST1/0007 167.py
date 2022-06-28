class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        r = len(numbers) - 1
        l = 0

        while (numbers[r] + numbers[l] != target):
            if numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1

        return [l + 1, r + 1]