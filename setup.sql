-- Create the user table --

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

-- Insert test records --

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Edgar",
    "Castillo",
    "Videogames"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Antonio",
    "Medina",
    "Books"
);