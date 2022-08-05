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

-- Create the vehicle table --

CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand VARCHAR(45),
    model VARCHAR(45),
    color VARCHAR(25),
    year INTEGER,
    userid INTEGER,
    active BOOLEAN DEFAULT 1,
    FOREIGN KEY (id) REFERENCES user(id)
);

-- Insert test records --

INSERT INTO vehicle (
    brand,
    model,
    color,
    year,
    userid
) VALUES (
    "Mitsubishi",
    "Lancer",
    "Red",
    2005,
    1
);

INSERT INTO vehicle (
    brand,
    model,
    color,
    year,
    userid
) VALUES (
    "Chrysler",
    "Cruiser",
    "Gray",
    2001,
    2
);