-- Part 1.5 update.sql
--
-- Submitted by: Write your Name here
--


-- add your UPDATE statements here

-- 1.5.1 Update Events
SET SQL_SAFE_UPDATES=0;
UPDATE `event` SET `type` = 'Social' WHERE time > '17:00:00';
SET SQL_SAFE_UPDATES=1;

-- 1.5.2 Update Comments
SET SQL_SAFE_UPDATES=0;
UPDATE `comment` SET `timestamp` = (SELECT `status` . `timestamp` + 1 second FROM status WHERE `id` = `comment` . `statusId`);
SET SQL_SAFE_UPDATES=1;
