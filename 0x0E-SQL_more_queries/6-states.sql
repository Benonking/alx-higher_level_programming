-- create hbtn_0d_usa and table states(
--id INT unique,auto generated cant be NULL PK
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR NOT NULL
);
