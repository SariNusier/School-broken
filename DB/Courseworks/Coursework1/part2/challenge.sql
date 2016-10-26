-- Part 2.2 challenge.sql
--
-- Submitted by: Write your Name here
--
--


-- add your SQL statements here
ALTER TABLE `k1333307db`.`status`
ADD COLUMN `attachment` LONGBLOB NULL;

CREATE TABLE `k1333307db`.`invitation` (
    `invitorId` INT NOT NULL,
    `inviteeId` INT NOT NULL,
    `eventId` INT NOT NULL,
    `accepted` BIT NULL,
    PRIMARY KEY (`invitorId`, `inviteeId`, `eventId`),
    CONSTRAINT `fk_invitor`
      FOREIGN KEY (`invitorId`)
      REFERENCES `k1333307db`.`employee` (`id`)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    CONSTRAINT `fk_invitee`
      FOREIGN KEY (`inviteeId`)
      REFERENCES `k1333307db`.`employee` (`id`)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    CONSTRAINT `fk_event`
      FOREIGN KEY (`eventId`)
      REFERENCES `k1333307db`.`event` (`id`)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);

delimiter $$
  create trigger `trigger_before_insert_invitation` before insert on `invitation`
  for each row
  begin
      declare error_msg varchar(128);
      if new.invitorId = new.inviteeId then
  		SET NEW.accepted = 1;
  	elseif new.invitorId != (SELECT `creatorId` FROM `event` WHERE `id` = NEW.eventId) THEN
          set error_msg = 'The event was not created by the invitor';
          signal sqlstate '45000' set message_text = error_msg;
      end if;
  end$$

  create trigger `trigger_before_update_invitation` before update on `invitation`
    for each row
    begin
        declare error_msg varchar(128);
        if new.accepted IS NULL then
            set error_msg = 'Cannot set accepted value to NULL';
            signal sqlstate '45000' set message_text = error_msg;
        end if;
    end$$

delimiter ;
