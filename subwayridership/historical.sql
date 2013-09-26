
DROP TABLE IF EXISTS subwaylines;
DROP TABLE IF EXISTS ridership;
DROP TABLE IF EXISTS stations;

CREATE TABLE stations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    borough ENUM('Manhattan', 'Brooklyn', 'Bronx', 'Staten Island', 'Queens'),
    name VARCHAR(255),
    subwaylines VARCHAR(255),
    ZipCode INT
);

CREATE TABLE ridership (
    station_id INT,
    year INT,
    riders INT,
    FOREIGN KEY (station_id) REFERENCES stations (id)
);

CREATE TABLE subwaylines ( 
    station_id INT,
    line VARCHAR(1),
    FOREIGN KEY (station_id) REFERENCES stations (id)
);

