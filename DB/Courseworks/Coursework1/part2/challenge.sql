-- Part 2.2 challenge.sql
--
-- Submitted by: Sari Nusier
--
--


-- add your SQL statements here

-- In order to attach other types of files to a status, a LONGBLOB field must be added
ALTER TABLE `status`
ADD COLUMN `attachment` LONGBLOB NULL;

-- One table is created for both allowing event creators to invite people, and
-- allowing any employee to confirm coming to an event.
-- This is achieved by having a nullable BIT field `confirmed`. An employee is allowed
-- to create invitations only if they've created the event, OR if they invite themselves.
-- If an employee invites themselves, the confirmed field MUST be 1, thus allowing
-- for any employee to confirm attendence to an event.
CREATE TABLE `invitation` (
    `invitorId` INT NOT NULL,
    `inviteeId` INT NOT NULL,
    `eventId` INT NOT NULL,
    `confirmed` BIT NULL,
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

-- The trigger makes sure that only event creators can invite others OR
-- if an employee invites themselves, the confirmed status is set to 1 by default.
-- Otherwise, display an error.
delimiter $$
  create trigger `trigger_before_insert_invitation` before insert on `invitation`
  for each row
  begin
      declare error_msg varchar(128);
      if new.invitorId = new.inviteeId then
  		SET NEW.confirmed = 1;
  	elseif new.invitorId != (SELECT `creatorId` FROM `event` WHERE `id` = NEW.eventId) THEN
          set error_msg = 'The event was not created by the invitor';
          signal sqlstate '45000' set message_text = error_msg;
      end if;
  end$$

-- The trigger makes sure that the confirmed status cannot be updated to NULL,
-- once it has been set to 0 or 1.
  create trigger `trigger_before_update_invitation` before update on `invitation`
    for each row
    begin
        declare error_msg varchar(128);
        if new.confirmed IS NULL then
            set error_msg = 'Cannot set confirmed value to NULL';
            signal sqlstate '45000' set message_text = error_msg;
        end if;
    end$$

delimiter ;
