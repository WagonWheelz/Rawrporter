FROM archlinux:latest
ENV DOCKER=false
ENV USERNAME=CHANGEME
ENV APP_PASSWORD=PASSWORD123

USER root

RUN <<EOF
    pacman --noconfirm -Sy python-pip
    mkdir /app
EOF

COPY ./src /app

RUN <<PIP
    cd /app
    pip install -r requirements.txt
PIP

LABEL version="1.0"

ENTRYPOINT ["/app/startup.sh"]
