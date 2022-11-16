DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS attendance;


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

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    members_id SERIAL NOT NULL REFERENCES members(id),
    sessions_id SERIAL NOT NULL REFERENCES sessions(id)
);
ALTER TABLE dbo.members DROP CONSTRAINT FK_





