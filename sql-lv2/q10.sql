-- 중복 제거하기
SELECT COUNT(*) as count FROM (
    SELECT * FROM ANIMAL_INS WHERE NAME IS NOT Null GROUP BY NAME 
) as a 