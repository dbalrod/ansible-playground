FROM mysql:8.0-debian
ARG MYSQL_USER

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends --fix-missing -y ssh sudo python3 pip \
    && apt-get clean \
    && pip install pymysql cryptography\
    && mkdir /run/sshd \
    && rm -rf /var/lib/apt/lists/* \
    && adduser ${MYSQL_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${MYSQL_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${MYSQL_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${MYSQL_USER}

COPY src/bin/new-docker-entrypoint.sh /
RUN chmod +x /new-docker-entrypoint.sh

EXPOSE 22 3306 33060 
ENTRYPOINT ["/new-docker-entrypoint.sh"]
CMD ["mysqld"]