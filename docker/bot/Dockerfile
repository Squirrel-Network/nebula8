FROM    python:alpine

WORKDIR /opt/service
USER    root

RUN apk add --no-cache \
            build-base \
            libffi-dev \
            mariadb-connector-c-dev

RUN apk add --no-cache \
            bash
RUN apk add --no-cache \
            git

# RUN     mkdir       ./data -p
COPY    scripts     ./scripts

ENV     NEBULA_HOME /opt/service/data

ENTRYPOINT [ "bash", "scripts/entrypoint.sh" ]
CMD [ "python3", "data/main.py" ]