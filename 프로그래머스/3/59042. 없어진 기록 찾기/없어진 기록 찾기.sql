
SELECT B.ANIMAL_ID,	B.NAME

FROM  ANIMAL_OUTS B
LEFT JOIN ANIMAL_INS A 
ON  B.ANIMAL_ID = A.ANIMAL_ID 
WHERE A.INTAKE_CONDITION IS NULL

