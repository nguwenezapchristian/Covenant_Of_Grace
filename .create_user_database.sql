-- Drop the sermon_audio database if it exists
DROP DATABASE IF EXISTS sermon_audio;

-- Create the sermon_audio database
CREATE DATABASE sermon_audio;

-- Create a MySQL user 'nguweneza' with password 'C704204p'
CREATE USER 'chris'@'localhost' IDENTIFIED BY 'C704204p';

-- Grant all privileges on the 'sermon_audio' database to the user 'nguweneza'
GRANT ALL PRIVILEGES ON sermon_audio.* TO 'nguweneza'@'localhost';

-- Apply the privileges
FLUSH PRIVILEGES;
