# LeetCode #3436 | Find Valid Emails | [EASY]
# [!] IMPORTANT: RegEx

SELECT * FROM Users 
WHERE REGEXP_LIKE(email,'^[a-zA-Z0-9_]+@[a-zA-Z]+\\.com$', 'i')
ORDER BY user_id 
