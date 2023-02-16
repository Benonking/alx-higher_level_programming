-- create table unique_if 
-- id INT with default 1 and must be unique
-- name VARCHAR (256)
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 PRIMARY_KEY,
	name VARCHAR(256)
);
