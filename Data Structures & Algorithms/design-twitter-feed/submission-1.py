class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # key = user Id, val = followeeIds
        self.tweetMap = defaultdict(list) # key = user Id, val = list[(count, tweetId)]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        newTweetId = tweetId
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
