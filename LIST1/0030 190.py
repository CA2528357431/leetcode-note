class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans<<1) | (n&1)
            n = n>>1
        return ans

    # (n&1)
    # 1 除了最后一位都是0
    # 保留最后一位

    # (ans << 1) | (n & 1)
    # (ans << 1) 最后一位是0
    # 改变最后一位