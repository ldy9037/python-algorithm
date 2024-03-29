-- 입양 시각 구하기 (1)
SELECT DATE_FORMAT(DATETIME, "%k") as HOUR, COUNT(*) as COUNT 
FROM ANIMAL_OUTS
WHERE DATE_FORMAT(DATETIME, "%k") >= 9 and DATE_FORMAT(DATETIME, "%k") < 20 
GROUP BY DATE_FORMAT(DATETIME, "%k")
ORDER BY HOUR*1 ASC