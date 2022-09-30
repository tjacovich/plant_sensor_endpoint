
#!/usr/bin/env bash
set -e
psql "postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST/$POSTGRES_DB?sslmode=disable" <<-EOSQL
    CREATE USER plant_sensor_endpoint WITH ENCRYPTED PASSWORD 'plant_sensor_endpoint';
    CREATE DATABASE plant_sensor_endpoint;
    CREATE DATABASE plant_sensor_endpoint_test;
    GRANT ALL PRIVILEGES ON DATABASE plant_sensor_endpoint TO plant_sensor_endpoint;
    GRANT ALL PRIVILEGES ON DATABASE plant_sensor_endpoint_test TO plant_sensor_endpoint;
EOSQL