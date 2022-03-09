-- creates the table force_name
-- force_name description: id INT name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    `id` INT UNIQUE NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);