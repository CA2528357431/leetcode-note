class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        mask_max = 3 ** numSlots

        dp = [0] * mask_max

        for mask in range(1, mask_max):
            cnt = 0
            m = mask

            for i in range(numSlots):
                cnt += m % 3
                m //= 3

            if cnt > n:
                continue
            # cnt 描述了一共放入的数字个数
            # 按照nums里的顺序放入

            m = mask
            w = 1
            for i in range(numSlots):
                num = m % 3
                # 此位的数字个数
                if num > 0:
                    dp[mask] = max(dp[mask], dp[mask - w] + (nums[cnt - 1] & (i + 1)))
                    # 回溯到放最后一个数字的状态
                    # dp
                m //= 3
                w *= 3

        return max(dp)