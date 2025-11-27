# LeetCode #3642 | Find Books with Polarized Opinions | [EASY]
# [!] IMPORTANT: Combined Queries

SELECT B.book_id, B.title, B.author, B.genre, B.pages,
        MAX(RS.session_rating)-MIN(RS.session_rating) AS rating_spread, 
        ROUND(((R.NRC+R.PRC) / COUNT(RS.book_id)), 2) AS polarization_score 
FROM books AS B
JOIN
(
    SELECT NegRS.book_id, NegRS.RC AS NRC, PosRS.RC AS PRC
    FROM
    (
        SELECT book_id, COUNT(session_id) AS RC FROM reading_sessions 
        WHERE session_rating <= 2
        GROUP BY book_id
        HAVING COUNT(session_id) >= 1
    ) AS NegRS
    JOIN 
    (
        SELECT book_id, COUNT(session_id) AS RC FROM reading_sessions 
        WHERE session_rating >= 4  
        GROUP BY book_id
        HAVING COUNT(session_id) >= 1
    ) AS PosRS
    ON PosRS.book_id = NegRS.book_id
) AS R
ON R.book_id = B.book_id
JOIN reading_sessions AS RS
ON B.book_id = RS.book_id
GROUP BY B.book_id
HAVING (COUNT(R.book_id) >= 5) AND (polarization_score >= 0.6)
ORDER BY polarization_score DESC, B.title DESC
