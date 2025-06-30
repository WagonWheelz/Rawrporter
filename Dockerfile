FROM archlinux:latest
ENV DOCKER="TRUE"
ENV USERNAME="CHANGEME"
ENV APP_PASSWORD="PASSWORD123"
ENV BOT_CYCLE="60"

USER root

COPY ./src /app

RUN <<EOF
    pacman --noconfirm -Sy python python-pip
    pip install --break-system-packages -r /app/requirements.txt
EOF

LABEL version="1.0"

ENTRYPOINT ["/app/startup.sh"]
