class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        st = -1
        cnt = 0
        n = len(arr)
        for ii in range(n):
            i = arr[ii]
            if i != 0:
                cnt += 1
            else:
                cnt += 2
            if cnt >= n:
                st = ii
                break
        sp = False
        if cnt == n + 1:
            sp = True

        w = n - 1
        if sp:
            arr[w] = 0
            st -= 1
            w -= 1

        for ii in range(st, -1, -1):
            if arr[ii] == 0:
                arr[w] = 0
                arr[w - 1] = 0
                w -= 2
            else:
                arr[w] = arr[ii]
                w -= 1


