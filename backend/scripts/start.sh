#!/usr/bin/env bash

postgres_ready () {
  nc -z -i 2 db 5432
}

until postgres_ready; do
  echo 'PostgreSQL is unavailable, waiting...'
done

echo 'PostgreSQL connection established, continuing...'


uvicorn main:app --host 0.0.0.0 --port 8000 --reload --workers 4
