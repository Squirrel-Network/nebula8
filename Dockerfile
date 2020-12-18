FROM python:3

ARG PROJECT_DIR=/opt/project

COPY . ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN pip install -r requirements.txt
