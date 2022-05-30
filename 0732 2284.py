class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dic = {}
        n = len(senders)
        for i in range(n):
            num = len(messages[i].split())
            u = senders[i]
            if u not in dic:
                dic[u] = 0
            dic[u] += num
        senders.sort(key=lambda x: (dic[x], x))
        return senders[-1]
