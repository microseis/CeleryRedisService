FROM nginxinc/nginx-unprivileged:1-alpine

WORKDIR /usr/src/app

COPY . .

COPY default.conf /etc/nginx/conf.d/default.conf
COPY uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN mkdir -p "/staticfiles"
RUN chmod 755 /staticfiles

USER nginx

RUN echo "Done with nginx Dockerfile"