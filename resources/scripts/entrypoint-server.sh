#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers 4



exit $?


