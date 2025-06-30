#!/bin/bash
echo "Running in Docker: " printenv $DOCKER
echo "BSKY Account: " printenv $USERNAME
echo "BSKY App Passwod: " printenv $APP_PASSWORD
/usr/bin/python /app/main.py
