import heapq


class Twitter:

    def __init__(self):
        self.txt = {}
        self.follows = {}
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.txt:
            self.txt[userId] = []
        self.txt[userId].append((self.t, tweetId, userId))
        self.t -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        li = []
        dic = {}
        if userId in self.txt:
            li.append(self.txt[userId][-1])
            dic[userId] = 1
        if userId not in self.follows:
            self.follows[userId] = set()
        for u in self.follows[userId]:
            if u in self.txt:
                heapq.heappush(li, self.txt[u][-1])
                dic[u] = 1
        res = []
        for i in range(10):
            if not li:
                break
            t, tId, uId = heapq.heappop(li)
            res.append(tId)
            if len(self.txt[uId]) > dic[uId]:
                dic[uId] += 1
                neo = dic[uId]
                heapq.heappush(li, self.txt[uId][-neo])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)