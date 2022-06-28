class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res = [None] * 3
        i = 0
        for c in nums:
            if i == 0 or c > res[i - 1]:
                res[i] = c
                i += 1
                if i == 3:
                    return True
            elif c < res[i - 1]:

                for j in range(i):
                    if c == res[j]:
                        break
                    elif j == 0 and c < res[j]:
                        res[j] = c
                        break
                    elif res[j] < c and c < res[j + 1]:
                        res[j + 1] = c
                        break
        return False

    # 同91思路
