# LeetCode #1050 | Actors and Directors Who Cooperated At Least Three Times | [EASY]

SELECT actor_id, director_id FROM ActorDirector 
GROUP BY actor_id, director_id 
HAVING COUNT(timestamp) > 2
ORDER BY actor_id, director_id