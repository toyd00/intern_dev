FROM --platform=linux/x86_64 mysql

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY sql_alchemy.py /tmp
