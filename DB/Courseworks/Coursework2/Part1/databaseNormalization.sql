-- Part 1.5 databaseNormalization.sql
--
-- Submitted by: Sari Nusier
--


--  Write your Database Normalization statements here


CREATE TABLE IF NOT EXISTS `crimeStatus` AS
	SELECT DISTINCT `status` AS 'status_code',
		`status_desc`
	FROM `crimes`;

ALTER TABLE `crimeStatus` ADD PRIMARY KEY(`status_code`);

CREATE TABLE IF NOT EXISTS `area` AS
	SELECT DISTINCT `area` AS 'area_code',
		`area_name`
	FROM `crimes`;

ALTER TABLE `crimeStatus` ADD PRIMARY KEY(`area_code`);
