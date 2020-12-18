#!/usr/bin/env bash

if [[ $DEBUG ]]
then
    set -x
fi

# source scripts/environment.sh
# source scripts/functions.sh

if [[ ! $(find $NEBULA_HOME -name ".init-*") ]]
then
    INIT_FILE="$NEBULA_HOME/.init-$(date "+%d%m%y%S%M%H")"
    touch $INIT_FILE
    {
        if [[ "$REPO" ]]
        then
            if [[ ! -d ./data ]]
            then
                git clone $REPO ./data

                echo "Install requirementes"
                pip3 install -r "data/requirements.txt"
            fi
        else
            echo "Can not initialize an empty container wihtout a source code. Please, set \$GIT_REPOSITORY for clone the code to execute."
            exit 449
        fi
    } || {
        mv $INIT_FILE "/var/log/$(basename $INIT_FILE)"
        exit $?
    }
fi

cat "scripts/templates/config.tmp.py" \
    | sed "s;%HOST%;$HOST;g" \
    | sed "s;%PORT%;$PORT;g" \
    | sed "s;%USER%;$USER;g" \
    | sed "s;%PASSWORD%;$PASSWORD;g" \
    | sed "s;%DBNAME%;$DBNAME;g" \
    \
    | sed "s;%BOT_TOKEN%;$BOT_TOKEN;g" \
    | sed "s;%SUPERADMIN%;$SUPERADMIN;g" \
    | sed "s;%OWNER%;$OWNER;g" \
    | sed "s;%DEFAULT_LOG_CHANNEL%;$DEFAULT_LOG_CHANNEL;g" \
    \
    | sed "s;%ENABLE_PLUGINS%;$ENABLE_PLUGINS;g" \
    | sed "s;%DEFAULT_LANGUAGE%;$DEFAULT_LANGUAGE;g" \
    | sed "s;%VERSION%;$VERSION;g" \
    | sed "s;%DEBUG%;$DEBUG;g" \
    \
    > "data/config.py"

cat "data/config.py"

exec "$@"