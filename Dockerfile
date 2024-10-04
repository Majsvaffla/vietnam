# Bullseye for linux/amd64
FROM python:3.11.2-slim@sha256:9ad4ffc502779e5508f7ac1eccab4a22786b80bd53d721d735f6de0840b245a1 AS base

RUN apt-get -qq update && apt-get -qqy install libpq-dev
RUN pip install --upgrade pip

FROM base as ci

WORKDIR /var/lib/vietnam

COPY dist dist

ENV PACKAGE_ROOT=/usr/local/lib/python3.11/site-packages

RUN pip wheel -q -w dist -r dist/requirements.txt
RUN pip install --no-cache --no-index --find-links=dist dist/*.whl
RUN python -m compileall -q ${PACKAGE_ROOT}
RUN rm dist/requirements.txt dist/*.whl

FROM ci AS runtime

ENV STATIC_ROOT=/var/lib/vietnam/static
ENV DIST_PATH=/var/lib/vietnam/dist
ENV LOGS_PATH=/var/log/vietnam

VOLUME ${STATIC_ROOT}
VOLUME ${LOGS_PATH}

EXPOSE 8000
