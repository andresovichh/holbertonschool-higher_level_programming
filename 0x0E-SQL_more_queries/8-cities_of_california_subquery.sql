--
--
SELECT state_id
FROM states
WHERE name == 'California';
SELECT id, name
FROM cities
WHERE hbtn_0d_usa(name) == 'California'
ORDER BY id ASC;