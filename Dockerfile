FROM nginx:alpine

COPY index.html /usr/share/nginx/html/
COPY welcome.html /usr/share/nginx/html/welcome.html
