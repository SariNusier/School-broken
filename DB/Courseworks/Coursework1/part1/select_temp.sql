-- Part 1.4 select.sql
--
-- Submitted by: Write your Name here
--


-- add your SELECT statements here

-- 1.4.1 Employee List.
SELECT `name`, `surname`, `email` from `employee`;

-- 1.4.2 Oldest Status.
SELECT `text` FROM `status` ORDER BY `timestamp` ASC limit 1 ;

-- 1.4.3 Total Usage.
SELECT FORMAT(SUM(`COUNT(*)`), 0)
FROM (
	SELECT COUNT(*) FROM `status`
    UNION
    SELECT COUNT(*) FROM `comment`
    UNION
    SELECT COUNT(*) FROM `event`
) AS allTables

-- 1.4.4 Event Report
SELECT type, FORMAT(COUNT(*), 0)
FROM `event`
WHERE MONTH(`date`) = 2
GROUP BY `type`;

-- 1.4.5 Comment Report


-- 1.4.6 Number 1 and 2


-- 1.4.7 Most Controversial Employee.
