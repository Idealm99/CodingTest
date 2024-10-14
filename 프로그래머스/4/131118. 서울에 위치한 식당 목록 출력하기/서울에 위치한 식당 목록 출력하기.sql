# SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS,
#        ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
# FROM REST_INFO I
# INNER JOIN REST_REVIEW R ON I.REST_ID = R.REST_ID
# WHERE I.ADDRESS LIKE '%서울%'
# GROUP BY I.REST_ID
# ORDER BY SCORE DESC, I.FAVORITES DESC;

select i.REST_ID,i.REST_NAME,i.FOOD_TYPE,i.FAVORITES,i.ADDRESS, round( avg(REVIEW_SCORE),2) as SCORE from REST_INFO i
inner join REST_REVIEW r on r.REST_ID  = i.REST_ID
where ADDRESS like '서울%'
group by r.REST_ID
order by SCORE desc, FAVORITES desc