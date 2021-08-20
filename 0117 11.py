class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        big = 0
        while r > l:
            big = max(min(height[r], height[l]) * (r - l), big)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return big

    # 双指针移动会必然性的降低宽度
    # 因此我么们为了使水多，应提高水深
    # 如果移动高的边 h = min(neo,short)<=short 水深只会减少
    # 如果移动低的边 h = min(neo,high) 有机会变多
    # 因此移动低的一侧