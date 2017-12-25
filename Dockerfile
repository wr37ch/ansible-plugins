FROM sbeliakou/centos:6.7
MAINTAINER Uladzislau Hramovich (uladzislau_hramovich@epam.com)
RUN yum install -y httpd web-assets-httpd
EXPOSE 80
CMD httpd -DFOREGROUND
