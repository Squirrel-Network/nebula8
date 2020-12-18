FROM ubuntu

RUN apt-get update
RUN apt-get install -y \
            openssh-server
RUN apt-get install -y \
            net-tools
RUN apt-get install -y \
            git
RUN apt-get install -y \
            iproute2
RUN apt-get install -y \
            inotify-tools

RUN mkdir /opt/data -p
COPY scripts/ /opt/scripts

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]