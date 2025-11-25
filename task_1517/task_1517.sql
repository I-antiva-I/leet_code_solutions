# LeetCode #1517 | Find Users With Valid E-Mails | [EASY]

SELECT * FROM Users
WHERE REGEXP_LIKE(mail,'^[A-Za-z]{1}[a-zA-Z0-9_.-]*@leetcode\\.com$', 'c')
ORDER BY user_id 