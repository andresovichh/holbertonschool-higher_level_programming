-- creates the table force_name
-- force_name description: id INT name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS `unique_id`(
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);