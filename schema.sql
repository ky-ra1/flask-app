CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL,
    admin BOOLEAN NOT NULL DEFAULT FALSE,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(200) NOT NULL UNIQUE,
    passwords VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO users(
    first_name, last_name, username, email, passwords) VALUES
    ('Testing', 'Bot', 'Test_Bot', 'testbot@testbot.com', '87a89s7da9s87djhajshdahsda8789as7daxcx%^%^57as');

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    user_id INTEGER NOT NULL, 
    CONSTRAINT messages_user_id_fk FOREIGN KEY (user_id) REFERENCES users (id)
);


