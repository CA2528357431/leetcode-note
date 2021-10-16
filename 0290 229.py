class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        a = None
        an = 0
        b = None
        bn = 0

        for i in nums:

            if (a is not None and i == a) or (b is not None and i == b):
                if (a is not None and i == a):
                    an += 1
                elif (b is not None and i == b):
                    bn += 1

            elif a is None or b is None:
                if a is None:
                    a = i
                    an = 1
                elif b is None:
                    b = i
                    bn = 1
            else:
                # i!=a and i!=b
                an -= 1
                if an == 0:
                    a = None
                bn -= 1
                if bn == 0:
                    b = None
        ndic = {}
        if a is not None:
            ndic[a] = 0
        if b is not None:
            ndic[b] = 0

        for i in nums:
            if i in ndic:
                ndic[i] += 1
        return [k for k in ndic.keys() if ndic[k] > n // 3]

    # 摩尔计数法