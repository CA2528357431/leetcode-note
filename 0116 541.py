class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slow = -1
        li = list(s)
        for f in range(len(li)):
            if f - slow == 2 * k:
                for r in range(k // 2):
                    li[slow + 1 + r], li[f - k - r] = li[f - k - r], li[slow + 1 + r]
                slow = f

        if len(li) - 1 - slow < k:
            for r in range((len(li) - slow) // 2):
                li[slow + 1 + r], li[len(li) - 1 - r] = li[len(li) - 1 - r], li[slow + 1 + r]
        elif len(li) - 1 - slow >= k:
            for r in range(k // 2):
                li[slow + 1 + r], li[slow + k - r] = li[slow + k - r], li[slow + 1 + r]

        res = "".join(li)
        return res