#!/usr/bin/env sh

if [ -n "$DEBUG" ]
then
    set -x
fi

echo "Waiting for agent"
sleep 1

TIME=1
while [ $(find "/opt/data" | grep lock) ]
do
    echo "Waiting for agent [n. $TIME]"
    sleep 1
    TIME=$(expr $TIME + 1)

    if [[ "$TIME" == "300" ]]
    then
        exit 500
    fi
done

exec "$@"

echo "Install requirementes"
pip3 install -r "/opt/data/repository/requirements.txt"

cat "/opt/scripts/templates/config.tmp.py" \
    | sed "s;%BOT_API%;$BOT_API;g" \
    | sed "s;%BOT_USER%;$BOT_USER;g" \
    | sed "s;%BOT_NAME%;$BOT_NAME;g" \
    | sed "s;%AUTHOR%;$AUTHOR;g" \
    | sed "s;%VERSION%;$VERSION;g" \
    | sed "s;%SOURCE%;$SOURCE;g" \
    \
    | sed "s;%STAFF_GROUP%;$STAFF_GROUP;g" \
    | sed "s;%ADMIN_ID%;$ADMIN_ID;g" \
    | sed "s;%OWNER%;$OWNER;g" \
    | sed "s;%LOG_CHANNEL%;$LOG_CHANNEL;g" \
    \
    | sed "s;%YANDEX_API%;$YANDEX_API;g" \
    | sed "s;%OPENWEATHER_API%;$OPENWEATHER_API;g" \
    \
    | sed "s;%DATABASE_SERVER%;$DATABASE_SERVER;g" \
    | sed "s;%DATABASE_USERNAME%;$DATABASE_USERNAME;g" \
    | sed "s;%DATABASE_PASSWORD%;$DATABASE_PASSWORD;g" \
    | sed "s;%DATABASE_NAME%;$DATABASE_NAME;g" \
    \
    > "/opt/data/repository/config.py"

python3 "/opt/scripts/main.py"
