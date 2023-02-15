-- import sql table dump temperatues.sql
-- display max temp of each state ordered by statename
SELECT state, MAX(value) as 'max_temp' FROM temperatures GROUP BY state ORDER BY state;
