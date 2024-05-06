CREATE TABLE IF NOT EXISTS users (
    PersonID BIGSERIAL NOT NULL PRIMARY KEY,
    UserName varchar(20) NOT NULL,
    UserPassword varchar(20) NOT NULL,
    Email varchar(50) NOT NULL
);