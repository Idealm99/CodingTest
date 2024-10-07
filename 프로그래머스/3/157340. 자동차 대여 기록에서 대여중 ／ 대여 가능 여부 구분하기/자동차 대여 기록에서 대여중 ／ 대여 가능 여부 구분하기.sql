# SELECT *
# FROM (
#     SELECT  CAR_ID, START_DATE, END_DATE 
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
#     ORDER BY END_DATE DESC
# ) AS RentalHistory -- 서브쿼리에 별칭을 부여
# GROUP BY CAR_ID

# ORDER BY CAR_ID
SELECT 
    CAR_ID, 
    CASE 
        WHEN COUNT(CASE 
                    WHEN START_DATE <= DATE('2022-10-16') AND DATE('2022-10-16') <= END_DATE 
                    THEN 1 
                    ELSE NULL 
                  END) > 0 
        THEN '대여중' 
        ELSE '대여 가능' 
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY 
GROUP BY 
    CAR_ID
ORDER BY 
    CAR_ID DESC;