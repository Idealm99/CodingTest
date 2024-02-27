-- 코드를 입력하세요
SELECT LEFT(product_code,2) AS CATEGORY, COUNT(*) AS PRODUCTS   FROM PRODUCT 
GROUP BY LEFT(product_code,2)
# HAVING COUNT(*) > 1 
