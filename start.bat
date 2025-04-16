@echo off

REM Run migrations
python manage.py migrate

REM Start the server with gunicorn
gunicorn meetupsite.wsgi:application --bind 0.0.0.0:%PORT%
