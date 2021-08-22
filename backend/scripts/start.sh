#!/usr/bin/sh

mongo_ready () {
  nc -zv -i 2 mongo 27017
}

until mongo_ready; do
  echo 'MongoDB is unavailable, waiting...'
done

echo 'MongoDB connection established, continuing...'


uvicorn main:app --host 0.0.0.0 --port 8000 --reload --workers 4