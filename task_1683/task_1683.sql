# LeetCode #1683 | Invalid Tweets | [EASY]

SELECT tweet_id  FROM Tweets
WHERE LENGTH(content) > 15;


# (+) Alternative solution.
#
# SELECT tweet_id  FROM Tweets
# WHERE content LIKE "________________%"