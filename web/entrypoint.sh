#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "mySQL started"
fi

python manage.py create_db
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
echo "Entry point working"

exec "$@"
