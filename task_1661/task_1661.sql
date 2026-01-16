# LeetCode #1661 | Average Time of Process per Machine | [EASY]

SELECT ActS.machine_id, ROUND(AVG(ActE.timestamp - ActS.timestamp), 3) AS processing_time FROM Activity AS ActS
JOIN Activity AS ActE
ON (ActS.machine_id = ActE.machine_id) AND (ActS.process_id = ActE.process_id)
WHERE (ActS.activity_type = "start") AND (ActE.activity_type = "end")
GROUP BY ActS.machine_id
