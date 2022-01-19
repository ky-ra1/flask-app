CREATE TABLE users (
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(200) UNIQUE,
    passwords VARCHAR(255) NOT NULL UNIQUE,
);

INSERT INTO users(
    first_name, last_name, username, email, passwords) VALUES
    (1, 'Testing', 'Bot', 'Test_Bot', testbot@testbot.com, '87a89s7da9s87djhajshdahsda8789as7daxcx%^%^57as');


-- CREATE TABLE  (
    id 

);


INSERT INTO  (
    .... ) VALUES 
    (1, '', '', )
)





-- CREATE TABLE admin (
--     id SERIAL PRIMARY KEY,
--     admin NOT NULL BOOLEAN,
-- )

