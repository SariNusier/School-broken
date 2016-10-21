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
  1,
  2,
  1,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  2,
  3,
  1,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  3,
  2,
  2,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  4,
  1,
  2,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  5,
  3,
  3,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  6,
  1,
  3,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  7,
  3,
  4,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  8,
  1,
  4,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  9,
  1,
  5,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  10,
  2,
  5,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  11,
  3,
  6,
  'Wow, glad to hear it.',
  '20160523091528');


INSERT INTO `comment` VALUES (
  12,
  2,
  6,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  13,
  1,
  7,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  14,
  2,
  7,
  'Wow, glad to hear it.',
  '20160523091528');

  INSERT INTO `comment` VALUES (
  15,
  3,
  8,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  16,
  2,
  8,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  17,
  3,
  9,
  'Wow, glad to hear it.',
  '20160523091528');

INSERT INTO `comment` VALUES (
  18,
  1,
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
  4);

INSERT INTO `likeComment` VALUES (
  2,
  5);

INSERT INTO `likeStatus` VALUES (
  2,
  1);

INSERT INTO `likeStatus` VALUES (
  2,
  2);

--

INSERT INTO `likeComment` VALUES (
  3,
  9);

INSERT INTO `likeComment` VALUES (
  3,
  10);

INSERT INTO `likeStatus` VALUES (
  3,
  3);

INSERT INTO `likeStatus` VALUES (
  3,
  6);


-- 3 business events January and February 2016
INSERT INTO `event` VALUES (
  1,
  1,
  'Social',
  'Cool event',
  '2016-01-12',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  2,
  2,
  'Social',
  'Cool event',
  '2016-02-13',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  3,
  3,
  'Social',
  'Cool event',
  '2016-01-25',
  '20:11:00',
  'Some nice place');
-- 3 Social events January and February 2016

INSERT INTO `event` VALUES (
  4,
  1,
  'Business',
  'Cool event',
  '2016-02-03',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  5,
  2,
  'Business',
  'Cool event',
  '2016-01-16',
  '20:11:00',
  'Some nice place');

INSERT INTO `event` VALUES (
  6,
  3,
  'Business',
  'Cool event',
  '2016-02-11',
  '20:11:00',
  'Some nice place');
