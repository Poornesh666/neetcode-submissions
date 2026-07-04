class Twitter:

    def __init__(self):
        self.user_store = defaultdict(list) #user_id: [(time, tweet_ids)]
        self.follower_store = defaultdict(set) #follower_id: {folowee_ids}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_store[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_ids = self.user_store[userId].copy()

        if userId in self.follower_store:
            folowee_list = self.follower_store[userId]

            for follower in folowee_list:
                if follower == userId: continue

                if follower in self.user_store:
                    tweet_ids.extend(self.user_store[follower])

        tweet_ids = [(-time, id) for time, id in tweet_ids]
        heapq.heapify(tweet_ids)

        ans = []
        while tweet_ids and len(ans) < 10:
            time, t_id = heapq.heappop(tweet_ids)
            ans.append(t_id)

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_store[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_store[followerId]:
            self.follower_store[followerId].remove(followeeId)

        
