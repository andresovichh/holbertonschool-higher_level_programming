-- all records of the table second_table
-- Don’t list rows without a name, lst score & name, DESC
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC
