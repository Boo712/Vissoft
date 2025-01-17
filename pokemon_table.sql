CREATE DATABASE IF NOT EXISTS pokemon;
USE pokemon;

CREATE TABLE IF NOT EXISTS pokemon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    type1 VARCHAR(50) NOT NULL,
    type2 VARCHAR(50),
    total INT NOT NULL,
    hp INT NOT NULL DEFAULT 0,
    attack INT NOT NULL DEFAULT 0,
    defense INT NOT NULL DEFAULT 0,
    spatk INT NOT NULL DEFAULT 0,
    spdef INT NOT NULL DEFAULT 0,
    speed INT NOT NULL DEFAULT 0,
    generation INT NOT NULL,
    legendary BOOLEAN NOT NULL
);

LOAD DATA LOCAL INFILE 'E:/Intern_Vissoft/Week_2/pokemon.csv'
INTO TABLE pokemon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, name, type1, type2, total, hp, attack, defense, spatk, spdef, speed, generation, legendary);