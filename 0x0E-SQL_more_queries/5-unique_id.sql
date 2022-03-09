-- creates the table force_name
-- force_name description: id INT name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS `id_not_null`(
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
);