#!/bin/bash
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

# uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload --reload-dir core --reload-dir config
gunicorn config.wsgi:application -b 0.0.0.0:8000 --workers $(($(nproc) * 2 + 1))


exit $?


