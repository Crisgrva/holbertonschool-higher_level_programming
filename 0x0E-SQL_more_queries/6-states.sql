--  Script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.`states` (
    `id` INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL,
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
