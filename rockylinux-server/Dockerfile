FROM rockylinux:8
ARG ROCKY_USER
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN yum -y update \
    && yum install -y openssh-clients openssh-server sudo python3 python3-pip \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${ROCKY_USER} -u "5000" \
    && echo "${ROCKY_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${ROCKY_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${ROCKY_USER}
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"] 
COPY src/bin/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]