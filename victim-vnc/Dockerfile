FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

MAINTAINER Rajesh Kalyanam "rkalyanapurdue@gmail.com"

#add utilities to run ping and traceroute
RUN apt-get update && apt-get -y install inetutils-ping=2:1.9.4-3 inetutils-traceroute=2:1.9.4-3

#create a non-root user
RUN useradd -d /home/victim -m -s /bin/bash victim

RUN echo 'victim:victim' | chpasswd

ENV USER=victim \
    PASSWORD=victim 
