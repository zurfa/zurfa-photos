--
-- File generated with SQLiteStudio v3.1.0 on Mi. Okt. 5 17:25:27 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: library
CREATE TABLE library (
    id        INTEGER          PRIMARY KEY,
    ufid      VARCHAR (10)     UNIQUE
                               NOT NULL,
    path      VARCHAR (128)    NOT NULL,
    origin    VARCHAR (64),
    size      INTEGER (8),
    checksum  VARCHAR (40),
    added     INTEGER (10),
    updated   INTEGER (10),
    extension VARCHAR (7),
    format    VARCHAR (10),
    category  VARCHAR (10),
    taken     INTEGER (10),
    lat       DECIMAL (15, 11),
    lon       DECIMAL (15, 11),
    device    VARCHAR (32),
    width     INTEGER (5),
    height    INTEGER (5) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
