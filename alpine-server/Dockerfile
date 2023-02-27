FROM alpine:3
ARG ALPINE_USER
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache --update openssh python3 sudo \
    && rm  -rf /tmp/* /var/cache/apk/* \
    && rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key \
    && ssh-keygen -A \
    && adduser ${ALPINE_USER} -u "5000" --disabled-password --gecos "" \
    && echo "${ALPINE_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${ALPINE_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${ALPINE_USER}
CMD ["/usr/sbin/sshd","-D"]