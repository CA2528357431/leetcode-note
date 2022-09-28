class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2 ** 4):
            # i表示案件状态
            pressArr = [(i >> j) & 1 for j in range(4)]
            # 获取每一位

            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = 0
                if n >= 1:
                    neo = (pressArr[0] + pressArr[1] + pressArr[3]) % 2
                    status |= neo << 0
                    # 1号点击状态
                if n >= 2:
                    neo = (pressArr[0] + pressArr[1]) % 2
                    status |= neo << 1
                if n >= 3:
                    neo = (pressArr[0] + pressArr[2]) % 2
                    status |= neo << 2
                if n >= 4:
                    neo = (pressArr[0] + pressArr[1] + pressArr[3]) % 2
                    status |= neo << 3
                seen.add(status)
        return len(seen)
