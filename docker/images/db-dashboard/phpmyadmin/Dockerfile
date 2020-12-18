FROM phpmyadmin/phpmyadmin

RUN apt-get update \
 && apt-get install -y \
            iproute2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /opt/data -p
COPY scripts/ /opt/scripts

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "apache2-foreground" ]