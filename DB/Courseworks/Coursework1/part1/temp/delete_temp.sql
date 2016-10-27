-- Part 1.6 delete.sql
--
-- Submitted by: Sari Nusier
--
--


-- add your DELETE statements here
SET SQL_SAFE_UPDATES=0;
DELETE FROM `employee` WHERE `email` = 'liam@neeson.com';
SET SQL_SAFE_UPDATES=1;
