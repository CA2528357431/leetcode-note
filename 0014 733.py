class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """



        # DFS
        '''
        old = image[sr][sc]
        if newColor != image[sr][sc]:
            image[sr][sc] = newColor
            for y,x in ((sr+1,sc),(sr-1,sc),(sr,sc+1),(sr,sc-1)):
                if -1<y<len(image) and -1<x<len(image[0]):
                    if image[y][x] == old:
                        image = self.floodFill(image, y, x, newColor)
        return image
        '''

        # BFS

        if newColor == image[sr][sc]:
            return image

        old = image[sr][sc]
        queue = [(sr, sc)]
        while queue:
            neo = []
            for x, y in queue:
                image[x][y] = newColor
                for xx, yy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= xx < len(image) and 0 <= yy < len(image[0]):
                        if image[xx][yy] == old:
                            neo.append((xx, yy))

            queue = neo
        return image




sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))