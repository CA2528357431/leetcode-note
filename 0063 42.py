class Solution:
    def trap(self, height):

        if len(height) < 3:
            return 0

        left = [0] * len(height)
        left[0] = height[0]
        right = [0] * len(height)
        right[-1] = height[-1]
        for x in range(1, len(height)):
            left[x] = max(left[x - 1], height[x])
        for x in range(len(height) - 1)[::-1]:
            right[x] = max(right[x + 1], height[x])

        water = 0
        for x in range(len(height)):
            water += min(left[x], right[x]) - height[x]

        return water






