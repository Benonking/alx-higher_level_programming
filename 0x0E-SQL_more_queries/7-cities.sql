-- creates a db hbtn_usa and table cities
-- table description
--     cites(id int outo increment not null primary key
--     state_id INT  cant be null foerign key)
-- script shoul not fail if db or table doesnt exist


CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

/* create cities table */
CREATE TABLE IF NOT EXISTS cities (
	   PRIMARY KEY(id),
	   id		INT UNIQUE AUTO_INCREMENT NOT NULL,
	   state_id INT 	   				  NOT NULL,
	   name 	VARCHAR(256),
	   FOREIGN KEY (state_id) REFERENCES states(id)
);
	
