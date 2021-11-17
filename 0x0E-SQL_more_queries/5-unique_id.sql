--  Script that creates the table force_name on your MySQL server.
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;
