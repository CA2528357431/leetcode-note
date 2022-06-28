class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = [x for x in range(k)]
        busy = []
        requests = [0] * k
        n = len(arrival)
        for i in range(n):
            t = load[i]
            start = arrival[i]
            while busy and busy[0][0] <= start:
                # 弹出已经结束的服务器
                end, idx = heappop(busy)
                neoidx = 0
                if idx % k < i % k:
                    neoidx = (i // k + 1) * k + idx % k
                else:
                    neoidx = (i // k) * k + idx % k
                # 新的index 既要同余维持性质，又要比当前的i大--为了在available中排在后面
                # available中的idx都是在i~i+n-1内
                heappush(available, neoidx)

            if available:
                idx = heappop(available) % k
                requests[idx] += 1
                heappush(busy, (start + t, idx))

        big = max(requests)
        return [x for x in range(k) if requests[x] == big]