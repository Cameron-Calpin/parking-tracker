-- CREATE DATABASE IF NOT EXISTS schema_test;

-- CREATE TABLE IF NOT EXISTS parking_tracker.indicator (
-- 	park_id  CHAR(20)      DEFAULT ''     NOT NULL,
--     park_status INT UNSIGNED  DEFAULT '0' NOT NULL,
--     PRIMARY KEY(park_id, park_status));
-- INSERT INTO schema_test.shop VALUES
--     (1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),
--     (3,'C',1.69),(3,'D',1.25),(4,'D',19.95);
--     
-- INSERT IGNORE INTO parking_tracker.indicator VALUES ('0'), ('1'), ('2'), ('3');
--     
-- -- SELECT * FROM schema_test.shop;

SELECT * FROM parking_tracker.indicator;