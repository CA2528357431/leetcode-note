class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        index = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                index = i
                break
        if index < 0:
            return False

        l = 0
        r = len(matrix[0]) - 1
        cur = matrix[index]
        while l < r:
            mid = (l + r) // 2
            if cur[mid] == target:
                return True
            elif target < cur[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return cur[l] == target