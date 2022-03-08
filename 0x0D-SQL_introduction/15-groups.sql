-- the number of records with the same score in the table second_table
-- display the score & nbr of records for this score with label number DESC
SELECT score, COUNT(score) As number FROM second_table GROUP BY score ORDER BY number DESC;
