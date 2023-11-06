CREATE TABLE IF NOT EXISTS parking (
    id SERIAL PRIMARY KEY,
    free_spaces INT NOT NULL,
    total_spaces INT NOT NULL,
    pk_name VARCHAR(255) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    reduced_capacity BOOLEAN NOT NULL,
    academico BOOLEAN NOT NULL,
    estudiante BOOLEAN NOT NULL,
    administrativo BOOLEAN NOT NULL,
    otro BOOLEAN NOT NULL,
    active BOOLEAN NOT NULL,
    last_update TIMESTAMP NOT NULL,
    estatica BOOLEAN NOT NULL
);
