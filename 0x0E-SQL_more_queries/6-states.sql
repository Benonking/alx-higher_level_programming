-- create hbtn_0d_usa and table states(
--id INT unique,auto generated cant be NULL PK
-- name VARCHAR(256)

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

/*create table*/
CREATE TABLE IF NOT EXISTS states (
       PRIMARY KEY(id),
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       name VARCHAR(256) NOT NULL
);
