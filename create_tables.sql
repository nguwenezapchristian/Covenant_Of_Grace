CREATE TABLE book_series_sermon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    verse_text TEXT,
    preached_by VARCHAR(255),
    audio VARCHAR(255) NOT NULL
);

CREATE TABLE scripture_sermon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    verse_text TEXT,
    preached_by VARCHAR(255),
    audio VARCHAR(255) NOT NULL
);

CREATE TABLE topic_sermon (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    verse_text TEXT,
    preached_by VARCHAR(255),
    audio VARCHAR(255) NOT NULL
);

