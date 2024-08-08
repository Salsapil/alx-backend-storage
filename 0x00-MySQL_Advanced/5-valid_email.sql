-- 5. Email validation to sent

DELIMITER //

CREATE TRIGGER reset_valid_email BEFORE FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;

//

DELIMITER;
