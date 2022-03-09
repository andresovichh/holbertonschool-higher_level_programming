--
--
SELECT state_id
FROM hbtn_0d_usa.states
WHERE name == 'California';
SELECT id, name
FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa(name) == 'California'
ORDER BY id ASC;