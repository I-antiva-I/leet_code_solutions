# LeetCode #3570 | Find Books with No Available Copies | [EASY]

SELECT B.book_id, B.title, B.author, B.genre, B.publication_year, B.total_copies AS "current_borrowers"
FROM library_books AS B
JOIN borrowing_records AS R ON B.book_id = R.book_id
WHERE R.return_date IS NULL
GROUP BY R.book_id
HAVING B.total_copies - COUNT(R.book_id) = 0
ORDER BY B.total_copies DESC, B.title ASC