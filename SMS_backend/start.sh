#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python manage.py runserver 0.0.0.0:8000
