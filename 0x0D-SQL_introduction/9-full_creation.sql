-- create table if doesn't exist
-- first_table creation
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` int,
    `name` varchar(256),
    `score` int
);
-- add rows
INSERT INTO 'second_table' (id, name)
VALUES ((1, 2, 3, 4), ('John', 'Alex', 'Bob', 'George'),
(10, 3, 14, 8))
