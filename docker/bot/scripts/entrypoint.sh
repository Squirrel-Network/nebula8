#!/usr/bin/env bash

if [[ $DEBUG ]]
then
    set -x
fi

# source scripts/environment.sh
# source scripts/functions.sh

if [[ ! $(find $SERVICE_HOME -name ".init-*") ]]
then
    INIT_FILE="$SERVICE_HOME/.init-$(date "+%d%m%y%S%M%H")"
    touch $INIT_FILE
    {
        if [[ "$REPO" ]]
        then
            if [[ ! -d $NEBULA_HOME ]]
            then
                git clone -b ${BRANCH:=master} $REPO $NEBULA_HOME | tee $INIT_FILE
                cd $NEBULA_HOME
                {
                    echo "Creating Virtual Environment" | tee $INIT_FILE
                    python3 -m venv env | tee $INIT_FILE

                    echo "Activate Virtual Environments" | tee $INIT_FILE
                    source env/bin/activate | tee $INIT_FILE

                    echo "Install requirementes" | tee $INIT_FILE
                    pip3 install -r "requirements.txt" | tee $INIT_FILE
                }
                cd /opt/service
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

cat "/opt/service/scripts/templates/config.tmp.py" \
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
    > "$NEBULA_HOME/config.py"

cat "$NEBULA_HOME/config.py"

cd $NEBULA_HOME
python3 main.py