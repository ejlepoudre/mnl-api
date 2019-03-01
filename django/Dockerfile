<<<<<<< HEAD
FROM python:3.6-alpine3.7

RUN ifconfig -a || ip a l

COPY requirements.txt /requirements.txt

RUN apk update && apk add bash gnupg yarn
RUN set -ex \
  && apk add --no-cache --virtual .build-deps \
=======
FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add bash
RUN set -ex \
  && apk add --no-cache \
>>>>>>> upstream/master
    gcc \
    make \
    libc-dev \
    musl-dev \
    linux-headers \
    pcre-dev \
    postgresql-dev \
    postgresql-client \
    python3-dev \
<<<<<<< HEAD
  && python3.6 -m venv /venv \
  && /venv/bin/pip install -U pip \
  && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
  && runDeps="$( \
    scanelf --needed --nobanner --recursive /venv \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --virtual .python-rundeps $runDeps \
  && apk del .build-deps

WORKDIR /srv/
COPY . .

RUN yarn install

EXPOSE 8000

ENTRYPOINT ["/srv/init.sh"]
=======
;

WORKDIR /srv/mnl
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
ENV PATH $PATH:/root/.local/bin
ENV PIP_NO_BINARY psycopg2
RUN set -ex && pipenv install --deploy --system

COPY . .
ENTRYPOINT ["./entrypoint.sh"]
>>>>>>> upstream/master
