CREATE TABLE IF NOT EXISTS flights (
    ...
);



-- Skapa tabell
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR,
    departure_time TIMESTAMP,
    arrival_time TIMESTAMP,
    departure_airport VARCHAR,
    destination_airport VARCHAR,
    airline VARCHAR
);

-- Infoga 3 exempelrader
INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport, airline)
VALUES
('SK123', '2025-07-01 08:00:00', '2025-07-01 10:30:00', 'ARN', 'LHR', 'SAS'),
('DY456', '2025-07-01 12:00:00', '2025-07-01 14:45:00', 'OSL', 'AMS', 'Norwegian'),
('LH789', '2025-07-01 15:30:00', '2025-07-01 18:15:00', 'FRA', 'CDG', 'Lufthansa');
