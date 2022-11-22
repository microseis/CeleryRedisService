FROM python:2.7.18-alpine

ENV PATH="/scripts:${PATH}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers libffi-dev libpq musl-dev zlib-dev libjpeg-turbo-dev
RUN pip install -r requirements.txt

RUN apk del .tmp
RUN apk add libjpeg
WORKDIR /usr/src/app

COPY . .

CMD ["entrypoint.sh"]

RUN echo "Done with web Dockerfile"