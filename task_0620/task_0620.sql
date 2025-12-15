# LeetCode #0620 | Not Boring Movies | [EASY]

SELECT * FROM Cinema
WHERE (id % 2 = 1) AND (description NOT LIKE "boring")
ORDER BY rating DESC
