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

RUN     mkdir           ./data
COPY    scripts         ./scripts

ENV     SERVICE_HOME    /opt/service/data
ENV     NEBULA_HOME     ${SERVICE_HOME}/nebula

ENTRYPOINT [ "bash", "/opt/service/scripts/entrypoint.sh" ]