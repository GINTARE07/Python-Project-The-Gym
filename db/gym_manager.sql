DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    membership_type VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT,
    part_of_day VARCHAR(255)
);

