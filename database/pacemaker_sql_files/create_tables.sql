-- ORDER 0 TABLES --
CREATE TABLE IF NOT EXISTS Account (
    username VARCHAR (50) PRIMARY KEY,
    password VARCHAR (50) NOT NULL CONSTRAINT "Password length must be between 3 and 50"
        CHECK(length(password) >= 3 AND length(password) <= 50)
);

CREATE TABLE IF NOT EXISTS Parameters (
    parameter VARCHAR(50) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS Mode (
    mode VARCHAR(50) PRIMARY KEY
);

-- ORDER 1 TABLES --
CREATE TABLE IF NOT EXISTS ModeParameters(
    mode            VARCHAR(50),
    parameter       VARCHAR(50),
    defaultValue    float8, -- match python float
    PRIMARY KEY (mode, parameter),
    -- safety critical systems should be very strict when deleting or updating modes and parameters.
    FOREIGN KEY (parameter)  references Parameters ON DELETE RESTRICT ON UPDATE RESTRICT,
    FOREIGN KEY (mode)       references Mode       ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- ORDER 2 TABLE --
CREATE TABLE IF NOT EXISTS AccountParameters(
    username    VARCHAR(50),
    parameter   VARCHAR(50),
    mode        VARCHAR(50),
    value       float8, -- match python float
    PRIMARY KEY (username, parameter, mode),
    FOREIGN KEY (username)         references Account         ON DELETE RESTRICT ON UPDATE RESTRICT,
    FOREIGN KEY (parameter, mode)  references ModeParameters ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- Function and Trigger for Account table, limit rows --
CREATE OR REPLACE FUNCTION check_number_of_rows()
RETURNS TRIGGER AS
$body$
BEGIN
    IF (SELECT count(*) FROM account) >= 10
    THEN
        RAISE EXCEPTION 'Cannot add an additional user, as 10 the user limit has been reached.';
    END IF;
    RETURN NEW;
END;
$body$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_check_number_of_rows
BEFORE INSERT ON account
FOR EACH ROW EXECUTE PROCEDURE check_number_of_rows();