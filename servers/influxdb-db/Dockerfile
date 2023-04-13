FROM influxdb:1.8-alpine
ARG INFLUXDB_USER

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache --update openssh python3 py3-pip sudo \
    && rm -rf /tmp/* /var/cache/apk/* \
    && rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key \
    && ssh-keygen -A \
    && adduser ${INFLUXDB_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${INFLUXDB_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${INFLUXDB_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${INFLUXDB_USER}

COPY src/bin/new-docker-entrypoint.sh /
RUN chmod +x /new-docker-entrypoint.sh

ENTRYPOINT ["/new-docker-entrypoint.sh"]
CMD ["influxd"]