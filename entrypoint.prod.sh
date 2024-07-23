#!/bin/sh

if [ "$DATABASE" = "bradrice_wt" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --settings=bradrice.settings.production
python manage.py migrate --settings=bradrice.settings.production
python manage.py collectstatic --settings=bradrice.settings.production --no-input --clear
python manage.py update_index --settings=bradrice.settings.production
exec "$@"
