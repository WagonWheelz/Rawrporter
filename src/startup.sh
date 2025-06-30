#!/bin/bash
time=$(date '+%Y-%m-%d %H:%M:%S.000000%z')
#export POSTED_DATE=$time
export POSTED_DATE='2025-06-30 02:00:00.000000+0000'
echo "Running in Docker: "$DOCKER
echo "Monitored RSS Feed: "$RSS_FEED
echo "BSKY Account: "$USERNAME
echo "BSKY App Passwod: "$APP_PASSWORD
echo "Starting Time: "$POSTED_DATE
echo "Executing bot run"
/usr/bin/python /app/main.py
