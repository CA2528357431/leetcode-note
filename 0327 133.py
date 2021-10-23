"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        '''
        # 图的广度优先
        used = {node}
        cur = [node]
        while cur:
            neo = []
            for no in cur:
                for ne in no.neighbors:
                    if ne not in used:
                        used.add(ne)
                        neo.append(ne)
            cur  = neo
        '''



        if not node:
            return None
        clone = Node(node.val)

        dic = {node: clone}
        used = {node}

        cur = [node]

        while cur:
            neo = []
            for no in cur:
                for ne in no.neighbors:
                    if ne not in dic:
                        nne = Node(ne.val)
                        dic[ne] = nne
                    dic[no].neighbors.append(dic[ne])
                    # 在clone中链接节点

                    if ne not in used:
                        neo.append(ne)
                        used.add(ne)
                    # 下一层节点

            cur = neo
        return dic[node]


