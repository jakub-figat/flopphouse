CREATE EXTENSION "uuid-ossp";

DROP DATABASE IF EXISTS test;
CREATE DATABASE test;

\c test
CREATE EXTENSION "uuid-ossp";