-- 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.


SELECT O.ANIMAL_ID, O.NAME 
FROM ANIMAL_OUTS O
LEFT OUTER JOIN ANIMAL_INS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID is NULL
ORDER BY O.ANIMAL_ID, O.NAME