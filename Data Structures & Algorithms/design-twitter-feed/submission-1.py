class Twitter:

    def __init__(self):
        self.user_store = {}
        self.follower_store = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_store:
            self.user_store[userId] = []

        self.user_store[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        if userId in self.user_store:
            res = self.user_store[userId].copy()

        if userId in self.follower_store:
            followee = self.follower_store[userId]
            for i in followee:
                if i == userId:
                    continue 
                if i in self.user_store:
                    res.extend(self.user_store[i])

        
        res.sort(reverse = True)
        res = res[:10]
        ans = []

        for time, news in res:
            ans.append(news)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_store:
            self.follower_store[followerId] = set()

        self.follower_store[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_store:
            if followeeId in self.follower_store[followerId]:
                self.follower_store[followerId].remove(followeeId)

        
