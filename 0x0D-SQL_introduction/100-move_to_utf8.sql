-- converts hbtn_0c_0 db to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE htbn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT to CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

