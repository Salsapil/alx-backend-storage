-- Write a SQL script that creates a table users with more columns

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY Key AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
