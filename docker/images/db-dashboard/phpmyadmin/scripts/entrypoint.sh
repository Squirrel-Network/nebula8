#!/usr/bin/env bash

if [ -n "$DEBUG" ]
then
    set -x
fi

if [ -n "$DATABASE_SERVER" ]
then
    export PMA_HOST="$DATABASE_SERVER"
else
    echo "No server provided!"
    exit 500
fi

if [ -n "$DATABASE_USERNAME" ]
then
    export PMA_USER="$DATABASE_USERNAME"
else
    echo "No user name provided!"
    exit 500
fi

if [ -n "$DATABASE_PASSWORD" ]
then
    export PMA_PASSWORD="$DATABASE_PASSWORD"
else
    echo "No user password provided!"
    exit 500
fi

IP=$(ip route get 8.8.8.8 | sed -n 's|^.*src \(.*\)$|\1|gp' | awk '{print $1}')
echo "Service IP Address: $IP"

exec /docker-entrypoint.sh "$@"