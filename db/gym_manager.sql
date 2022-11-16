DROP TABLE IF EXISTS members CASCADE;
DROP TABLE IF EXISTS sessions CASCADE;
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
    members_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    sessions_id INT NOT NULL REFERENCES sessions(id) ON DELETE CASCADE
);


