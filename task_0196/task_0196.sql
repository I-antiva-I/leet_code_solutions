# LeetCode #0196 | Delete Duplicate Emails | [EASY]

DELETE P1
FROM Person AS P1
JOIN Person AS P2
    ON P1.id > P2.id AND P1.email = P2.email
