FROM debian:stable
MAINTAINER support@trueability.com

EXPOSE 80
EXPOSE 443

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y apparmor-utils nginx-full php5-fpm && \
  rm -rf /etc/nginx/conf.d/* \
    /etc/nginx/sites-available/* \
    /var/www/cathealthcare.us && \
  echo "daemon off;" >> /etc/nginx/nginx.conf

ADD cathealthcare.conf /etc/nginx/conf.d/cathealthcare.conf
ADD cert.pem /etc/nginx/cert.pem
ADD chc.passwd /etc/nginx/chc.passwd
ADD cathealthcare.us /var/www/cathealthcare.us
ADD start.sh /usr/sbin/start.sh

CMD /usr/sbin/start.sh
