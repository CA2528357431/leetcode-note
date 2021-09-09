class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        def do(ang, length):
            if length <= 1:
                return
            for _ in range(length - 1):
                la = matrix[ang][ang]
                cur = [ang, ang + 1]

                while True:
                    neo = matrix[cur[0]][cur[1]]
                    matrix[cur[0]][cur[1]] = la
                    la = neo
                    # la,matrix[cur[0]][cur[1]] = matrix[cur[0]][cur[1]],la

                    if cur[0] == ang and cur[1] == ang:
                        break

                    if cur[0] == ang and cur[1] < ang + length - 1:
                        cur[1] += 1
                    elif cur[0] < ang + length - 1 and cur[1] == ang + length - 1:
                        cur[0] += 1
                    elif cur[0] == ang + length - 1 and cur[1] > ang:
                        cur[1] -= 1
                    elif cur[0] > ang and cur[1] == ang:
                        cur[0] -= 1

            do(ang + 1, length - 2)

        do(0, len(matrix))
        '''

        def do(ang, length):
            if length <= 1:
                print(matrix)
                return
            for x in range(length - 1):
                matrix[ang][ang + x], \
                matrix[ang + x][ang + length - 1], \
                matrix[ang + length - 1][ang + length - 1 - x], \
                matrix[ang + length - 1 - x][ang] \
                    = \
                matrix[ang + length - 1 - x][ang], \
                matrix[ang][ang + x], \
                matrix[ang + x][ang + length - 1], \
                matrix[ang + length - 1][ang + length - 1 - x]

            do(ang + 1, length - 2)

        do(0, len(matrix))