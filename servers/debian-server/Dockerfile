FROM debian:11
# TODO: Test if debian 11 works with all the examples. They were tested using debian 9
ARG DEBIAN_USER
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
    && apt-get install --no-install-recommends --fix-missing -y ssh sudo python3 python3-pip python3-apt \
    && apt-get clean \
    && mkdir /run/sshd \
    && rm -rf /var/lib/apt/lists/* \
    && adduser ${DEBIAN_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${DEBIAN_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${DEBIAN_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${DEBIAN_USER}
CMD ["/usr/sbin/sshd", "-D", "-e"]