-- creates database hbtn_0d_2 and user -> user_0d_2
-- user has only select privilege in db
-- user password -> user_0d_2_pwd
-- isdb already exists script should not fail
-- if user already exits script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

