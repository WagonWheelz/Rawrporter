FROM archlinux:latest
ENV DOCKER=false
ENV USERNAME=CHANGEME
ENV APP_PASSWORD=PASSWORD123

USER root

RUN <<EOF
    pacman --noconfirm -Syu --break-system-packages python python-pip
    mkdir /app
EOF

COPY ./src /app

RUN /usr/bin/pip install -r /app/requirements.txt

LABEL version="1.0"

ENTRYPOINT ["/app/startup.sh"]
