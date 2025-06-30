#!/bin/bash
echo "Running in Docker: "$DOCKER
echo "Monitored RSS Feed: "$RSS_FEED
echo "BSKY Account: "$USERNAME
echo "BSKY App Passwod: "$APP_PASSWORD
while true; do
    echo "Executing bot run"
    /usr/bin/python /app/main.py && wait
    echo "Waiting" $BOT_CYCLE "seconds till next run"
    sleep $BOT_CYCLE
done
