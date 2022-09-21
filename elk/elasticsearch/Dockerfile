ARG ELASTIC_VERSION
ARG TZ
# https://www.docker.elastic.co/
FROM docker.elastic.co/elasticsearch/elasticsearch:${ELASTIC_VERSION}
USER root
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ=${TZ} apt-get install -y tzdata
USER elasticsearch


# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install ingest-geoip
#RUN elasticsearch-plugin install ingest-geoip

