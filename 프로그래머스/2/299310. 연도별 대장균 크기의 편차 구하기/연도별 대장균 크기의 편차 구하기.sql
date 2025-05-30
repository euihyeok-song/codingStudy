SELECT 
       YEAR(A.DIFFERENTIATION_DATE) AS YEAR,
       B.MAX_SIZE - SIZE_OF_COLONY AS YEAR_DEV,
       A.ID AS ID
  FROM ECOLI_DATA A
  LEFT JOIN (SELECT 
                    YEAR(DIFFERENTIATION_DATE) AS DIFFERENTIATION_YEAR,
                    MAX(SIZE_OF_COLONY) AS MAX_SIZE
               FROM ECOLI_DATA
              GROUP BY YEAR(DIFFERENTIATION_DATE)) B
    ON YEAR(DIFFERENTIATION_DATE) = B.DIFFERENTIATION_YEAR
 ORDER BY YEAR ASC,
          YEAR_DEV ASC;