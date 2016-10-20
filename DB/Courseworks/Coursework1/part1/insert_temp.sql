-- Part 1.2 insert.sql
--
-- Submitted by: Write your Name here
--


-- add your INSERT statements here


-- 3 Celebrities as employees
INSERT INTO `employee` VALUES(1, 'Liam', 'Neeson', 'Male', '1952-06-07', 'liam@neeson.com');
INSERT INTO `employee` VALUES(2, 'Denzel', 'Washington', 'Male', '1954-12-28', 'denzel@washington.com');
INSERT INTO `employee` VALUES(3, 'Ellen', 'DeGeneres', 'Female', '1958-01-26', 'ellen@show.com');

-- 3 Statuses per employee
INSERT INTO `status` VALUES (
  1,
  1,
  'Hello everyone. Great day today!',
  '20160523091528');

INSERT INTO `status` VALUES (
  2,
  1,
  'Hello everyone. Great day today!',
  '20160524090204');

INSERT INTO `status` VALUES (
  3,
  1,
  'Hello everyone. Great day today!',
  '20160525091615');

--

INSERT INTO `status` VALUES (
  4,
  2,
  'Hello everyone. Great day today!',
  '20160310071615');

INSERT INTO `status` VALUES (
  5,
  2,
  'Hello everyone. Great day today!',
  '20160310071615');

INSERT INTO `status` VALUES (
  6,
  2,
  'Hello everyone. Great day today!',
  '20160310071615');

--

INSERT INTO `status` VALUES (
  7,
  3,
  'Hello everyone. Great day today!',
  '20160310071615');

INSERT INTO `status` VALUES (
  8,
  3,
  'Hello everyone. Great day today!',
  '20160310071615');

INSERT INTO `status` VALUES (
  9,
  3,
  'Hello everyone. Great day today!',
  '20160310071615');



-- 2 Comments per status

INSERT INTO `comment` VALUES (
  NULL,
  2,
  1,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  NULL,
  2,
  1,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  2,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  2,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  3,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  3,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  4,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  4,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  5,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  NULL,
  2,
  5,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  6,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  NULL,
  2,
  6,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  7,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  7,
  'Wow, glad to hear it.',
  '20160523091528');

  INSERT INTO `comment` VALUES (
  NULL,
  2,
  8,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  8,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  9,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  NULL,
  2,
  9,
  'Wow, glad to hear it.',
  '20160523091528');


-- 4 Likes per employee
INSERT INTO `likeComment` VALUES (
  1,
  1);

INSERT INTO `likeComment` VALUES (
  1,
  2);

INSERT INTO `likeStatus` VALUES (
  1,
  4);

INSERT INTO `likeStatus` VALUES (
  1,
  5);

--

INSERT INTO `likeComment` VALUES (
  2,
  3);

INSERT INTO `likeComment` VALUES (
  2,
  4);

INSERT INTO `likeStatus` VALUES (
  2,
  1);

INSERT INTO `likeStatus` VALUES (
  2,
  2);

--

INSERT INTO `likeComment` VALUES (
  3,
  5);

INSERT INTO `likeComment` VALUES (
  3,
  6);

INSERT INTO `likeStatus` VALUES (
  3,
  3);

INSERT INTO `likeStatus` VALUES (
  3,
  6);


-- 3 business events January and February 2016
INSERT INTO `event` VALUES (
  NULL,
  1,
  'Social',
  'Cool event',
  '2016-01-12',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  NULL,
  1,
  'Social',
  'Cool event',
  '2016-02-13',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  NULL,
  1,
  'Social',
  'Cool event',
  '2016-01-25',
  '20:11:00',
  'Some nice place');
-- 3 Social events January and February 2016

INSERT INTO `event` VALUES (
  NULL,
  1,
  'Business',
  'Cool event',
  '2016-02-03',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  NULL,
  1,
  'Business',
  'Cool event',
  '2016-01-16',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  NULL,
  1,
  'Business',
  'Cool event',
  '2016-02-11',
  '20:11:00',
  'Some nice place');
