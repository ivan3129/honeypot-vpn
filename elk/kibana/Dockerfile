ARG ELASTIC_VERSION
ARG TZ
# https://www.docker.elastic.co/
FROM docker.elastic.co/kibana/kibana:${ELASTIC_VERSION}
USER root
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ=${TZ} apt-get install -y tzdata
USER kibana

# Add your kibana plugins setup here
# Example: RUN kibana-plugin install <name|url>

