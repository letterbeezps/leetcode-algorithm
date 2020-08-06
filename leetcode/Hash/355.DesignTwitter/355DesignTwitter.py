class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = collections.defaultdict(list)  # userId -> list(tuple(time: int, twitterId: int))
        self.follows = collections.defaultdict(set)  # userId -> set(userId: int)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ps = []  # list(tuple(time: int, twitterId: int))
        for x in self.posts[userId]:
            ps.append(x)
        for follow in self.follows[userId]:
            for x in self.posts[follow]:
                ps.append(x)
        ps.sort(reverse=True)
        i, res = 0, []
        while i<10 and i<len(ps):
            res.append(ps[i][1])
            i += 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # if followeeId is not contained in the follows[followerId]
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)