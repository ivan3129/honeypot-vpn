ARG ELASTIC_VERSION
ARG TZ
# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELASTIC_VERSION}
#ENV DEBIAN_FRONTEND=noninteractive
# Add your logstash plugins setup here
# Example: RUN logstash-plugin install logstash-filter-json
USER root
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ=${TZ} apt-get install -y tzdata
USER logstash

RUN ls
