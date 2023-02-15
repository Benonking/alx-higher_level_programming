-- select all recoreds from second table
-- skip those without a name
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
