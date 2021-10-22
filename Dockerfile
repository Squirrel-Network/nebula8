# first stage
FROM python:3.9 AS builder
COPY requirements.txt .

# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# second unnamed stage
FROM python:3.9-slim
WORKDIR /app

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local
COPY . /app 

# update PATH environment variable
ENV PATH=/root/.local:$PATH

CMD [ "python", "./main.py" ]
