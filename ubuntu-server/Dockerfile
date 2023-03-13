FROM ubuntu:22.04
ARG UBUNTU_USER
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \ 
    && apt-get install --no-install-recommends -y ssh sudo python3 python3-pip \
    && apt-get clean \
    && mkdir /run/sshd \
    && rm -rf /var/lib/apt/lists/* \
    && adduser ${UBUNTU_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${UBUNTU_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${UBUNTU_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${UBUNTU_USER}
CMD ["/usr/sbin/sshd", "-D", "-e"]