FROM nginx:alpine

RUN mkdir -p /etc/certs

COPY ./resources/html/index.html /usr/share/nginx/html/
COPY ./resources/html/welcome.html /usr/share/nginx/html/welcome.html
COPY ./resources/certs /etc/certs
COPY ./resources/default.conf /etc/nginx/conf.d