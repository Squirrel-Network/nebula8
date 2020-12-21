#!/usr/bin/env bash

if [ -n "$DEBUG" ]
then
    set -x
fi

export MYSQL_RANDOM_ROOT_PASSWORD="yes"

if [ -n "$DATABASE_USERNAME" ]
then
    export MYSQL_USER="$DATABASE_USERNAME"
else
    echo "No user name provided!"
    exit 500
fi

if [ -n "$DATABASE_PASSWORD" ]
then
    export MYSQL_PASSWORD="$DATABASE_PASSWORD"
else
    echo "No user password provided!"
    exit 500
fi

if [ -n "$DATABASE_NAME" ]
then
    export MYSQL_DATABASE="$DATABASE_NAME"
else
    export MYSQL_DATABASE="nebula"
fi

for FILE in $(find /docker-entrypoint-initdb.d | grep -i "[.]sql")
do
    sed -i "s;%DATABASE%;$DATABASE_NAME;g" "$FILE"
done

IP=$(ip route get 8.8.8.8 | sed -n 's|^.*src \(.*\)$|\1|gp' | awk '{print $1}')
echo "Service IP Address: $IP"

exec docker-entrypoint.sh "$@"