--  Script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS `force_name` (
    `id` INT DEFAULT NULL,
    `name` VARCHAR(256)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
