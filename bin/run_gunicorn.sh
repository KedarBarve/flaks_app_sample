#!/bin/sh
gunicorn --bind 0.0.0.0:8008 --chdir /app/src/main server:gunicorn_app
