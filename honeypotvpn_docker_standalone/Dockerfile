FROM python:latest

LABEL Maintainer="Ivan Yuquilima"

WORKDIR /honeypotvpn


RUN git clone ivan3129/honeypot-vpn

COPY requirements.txt /tmp/

RUN pip3 install --upgrade -r /tmp/requirements.txt

RUN python3 setup.py install


