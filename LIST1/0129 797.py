class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # BFS
        '''
        n = len(graph)
        res = []
        temp = [[0]]
        for _ in range(n):
            neo = []
            for route in temp:
                if route[-1]==n-1:
                    res.append(route)
                else:
                    for x in graph[route[-1]]:
                        neo.append(route+[x])
            temp = neo

        return res
        '''

        #DFS
        res = []
        cur = [0]
        n = len(graph)
        def dfs(length,cur):
            if length>=n:
                return
            if cur[-1] == n-1:
                res.append(cur.copy())
            else:
                for x in graph[cur[-1]]:
                    cur.append(x)
                    dfs(length+1,cur)
                    cur.pop()
        dfs(0,cur)
        return res
