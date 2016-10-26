-- Part 1.3 view.sql
--
-- Submitted by: Write your Name here
--


-- add your CREATE VIEW statement here


-- add your statement to test rejection
CREATE VIEW `futureEventsView` AS
	SELECT * FROM `event` WHERE TIMESTAMP(`date`,`time`) > now()
WITH CHECK OPTION;

INSERT INTO `futureEventsView` VALUES (
 NULL,
 3,
 'Social',
 'Test futureEventsView',
 '2015-01-01',
 '11:11:00',
 'London'
);
