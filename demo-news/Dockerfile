FROM debian:stable
MAINTAINER support@trueability.com

EXPOSE 80

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y apparmor-utils nginx-full && \
  rm -rf /etc/nginx/conf.d/* \
    /etc/nginx/sites-available/* \
    /var/www/news.trulytech.net && \
  echo "daemon off;" >> /etc/nginx/nginx.conf

ADD news.trulytech.net.conf /etc/nginx/conf.d/news.trulytech.net.conf
ADD news /var/www/news

CMD service nginx start
