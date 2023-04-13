FROM mongo:6
ARG MONGO_USER

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends --fix-missing -y ssh sudo python3 pip \
    && apt-get clean \
    && pip install cryptography\
    && mkdir /run/sshd \
    && rm -rf /var/lib/apt/lists/* \
    && adduser ${MONGO_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${MONGO_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${MONGO_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${MONGO_USER}

COPY src/bin/new-docker-entrypoint.sh /
RUN chmod +x /new-docker-entrypoint.sh

ENTRYPOINT ["/new-docker-entrypoint.sh"]
CMD ["mongod"]