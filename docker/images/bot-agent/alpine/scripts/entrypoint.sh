#!/usr/bin/env bash

if [ -n "$DEBUG" ]
then
    set -x
fi

touch "/opt/data/agent.lock"

function updateRepository
{
    if [ -n "$REPOSITORY_URL" ]
    then
        echo "Check repository from $REPOSITORY_URL"
        if [ ! -d /opt/data ] || [ ! "$(ls -A /opt/data/repository)" ]
        then
            if [ -n $REPOSITORY_BRANCH ]
            then
                REPOSITORY_URL="-b $REPOSITORY_BRANCH $REPOSITORY_URL"
            fi

            git clone $REPOSITORY_URL /opt/data/repository
        else 
            cd /opt/data/repository
            git pull
            cd - > /dev/null
        fi
    elif [ -n "$LOCAL_VOLUME" ]
    then
        #mkdir /opt/data/repository -p
        cp /opt/data/local/. /opt/data/repository/ -ruv
    elif [ ! -d /opt/data/repository ] || [ ! "$(ls -A /opt/data/repository)" ]
    then
        exit 500
    fi
}

echo "Configuring root"
chsh --shell /bin/bash root

echo "Configuring sshd"
sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g" /etc/ssh/sshd_config

service ssh start
if [ -n "$SSH_PASSWORD" ]
then
    usermod -p `openssl passwd $SSH_PASSWORD` root
fi

updateRepository

if [ $# -gt 0 ]
then
    exec "$@"
fi

IP=$(ip route get 8.8.8.8 | sed -n 's|^.*src \(.*\)$|\1|gp' | awk '{print $1}')
echo "Service IP Address: $IP"

rm "/opt/data/agent.lock"

if [ -n "$LOCAL_VOLUME" ]
then
    while inotifywait -e modify -r /opt/data/local
    do
        updateRepository
    done
else
    while "true"
    do
        echo "Update not supported yet!"
        sleep 3600
    done
fi