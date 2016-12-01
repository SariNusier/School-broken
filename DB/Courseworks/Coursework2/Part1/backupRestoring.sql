-- Part 1.1 backupRestoring.sql
--
-- Submitted by: Sari Nusier
--


-- add your Backup Restoring statements here

-- connecting to calcium:
-- ssh k1333307@calcium.inf.kcl.ac.uk

-- Restoring database:
-- mysql -u k1333307 -p -h nmsdvm999956.nms.kcl.ac.uk k1333307db < crimes2015.sql
SOURCE crimes2015.sql;
