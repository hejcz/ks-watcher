FROM alpine:3.7
RUN apk add --no-cache python3 curl gcc libffi-dev python3-dev musl-dev openssl-dev bash \
  && pip3 install --upgrade pip \
  && pip3 install poetry \
  && mkdir /ks-watcher \
  && rm -rf /var/cache/apk/*

WORKDIR /ks-watcher

COPY pyproject.toml poetry.lock /ks-watcher/

RUN poetry env use python3 && poetry install

COPY . /ks-watcher

VOLUME history

ENTRYPOINT ["python3", "docker-entrypoint.py"]
