-- import into hbtn_0c_0 table dump(temperatures.sql)
-- then calculate avg temp(Fehrenheit) by city ordered by temp DESC
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
