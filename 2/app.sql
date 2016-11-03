--
-- File generated with SQLiteStudio v3.1.0 on Mi. Okt. 26 19:26:04 2016
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: hashes
CREATE TABLE hashes (
    uid      INTEGER      PRIMARY KEY,
    ufid     VARCHAR (10) UNIQUE,
    checksum VARCHAR (40) 
);


-- Table: items
CREATE TABLE items (
    uid       INTEGER      PRIMARY KEY,
    ufid      VARCHAR (10) UNIQUE,
    status    BOOLEAN      DEFAULT True,
    path      STRING (256),
    origin    STRING (64),
    size      INTEGER (12),
    added     INTEGER (10),
    updated   INTEGER (10),
    extension VARCHAR (8),
    format    VARCHAR (16),
    category  VARCHAR (10) 
);


-- Table: metadata
CREATE TABLE metadata (
    uid    INTEGER      PRIMARY KEY,
    ufid   VARCHAR (10) UNIQUE,
    width  INTEGER (5),
    height INTEGER (5) 
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
