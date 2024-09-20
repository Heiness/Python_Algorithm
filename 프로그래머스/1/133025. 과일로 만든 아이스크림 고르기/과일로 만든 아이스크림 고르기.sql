SELECT a.FLAVOR
FROM FIRST_HALF a JOIN ICECREAM_INFO b
ON a.FLAVOR = b.FLAVOR
WHERE TOTAL_ORDER > 3000
    AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC