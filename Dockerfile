FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps


RUN mkdir /festivals
WORKDIR /festivals
COPY . .
COPY festivals/entrypoint.sh .

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user
EXPOSE 8000
ENTRYPOINT ["festivals/entrypoint.sh"]
USER user