FROM mysql

RUN apt-get update \
 && apt-get install -y \
            iproute2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN ln -s /var/lib/mysql /opt/data
COPY scripts/ /opt/scripts
COPY sql/ /docker-entrypoint-initdb.d

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "mysqld" ]