ARG TZ
FROM python:latest

LABEL Maintainer="Ivan Yuquilima"

WORKDIR /honeypotvpn


RUN git clone https://github.com/ivan3129/honeypot-vpn.git

WORKDIR honeypot-vpn


RUN python3 setup.py install


