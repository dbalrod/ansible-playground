FROM postgres:11-alpine
ARG PSQL_USER

# add openssh and clean g
RUN apk update && apk add --no-cache --update openssh sudo python3 py3-pip \
    && rm  -rf /tmp/* /var/cache/apk/* \
    && pip install psycopg2-binary \
    && rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key \
    && ssh-keygen -A \
    && adduser ${PSQL_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${PSQL_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "postgres:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${PSQL_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${PSQL_USER}

COPY src/bin/new-docker-entrypoint.sh /
RUN chmod +x /new-docker-entrypoint.sh

ENTRYPOINT ["/new-docker-entrypoint.sh"]
CMD ["postgres"]