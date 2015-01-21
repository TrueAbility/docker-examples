FROM debian:stable
MAINTAINER support@trueability.com

EXPOSE 80

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y apparmor-utils nginx-full && \
  rm -rf /etc/nginx/conf.d/* \
    /etc/nginx/sites-available/* \
    /var/www/media.rivercity.co && \
  echo "daemon off;" >> /etc/nginx/nginx.conf

ADD media.rivercityco.net.conf /etc/nginx/conf.d/media.rivercityco.net.conf
ADD media /var/www/media

CMD service nginx start
