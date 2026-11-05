import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0

        # user -> list of (time, tweetId)
        self.tweets = defaultdict(list)

        # user -> set of followed users
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # Include user's own tweets
        users = set(self.following[userId])
        users.add(userId)

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index - 1)
                )

        result = []

        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            if index >= 0:
                time, nextTweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-time, nextTweetId, uid, index - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)