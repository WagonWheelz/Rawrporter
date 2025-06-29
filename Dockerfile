FROM archlinux:latest
ENV DOCKER=false
ENV USERNAME=CHANGEME
ENV APP_PASSWORD=PASSWORD123

USER root

RUN <<EOF
    pacman --noconfirm -Sy --break-system-packages python3 python-pip
    mkdir /app
EOF

COPY ./src /app

RUN python -m pip install -r /app/requirements.txt

LABEL version="1.0"

ENTRYPOINT ["/app/startup.sh"]
