FROM rockylinux:8
ARG ROCKY_USER
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN yum -y update && yum clean all \
    && yum -y install systemd \
    && yum clean all \
    && for i in /lib/systemd/system/sysinit.target.wants/*; do [ "${i##*/}" = systemd-tmpfiles-setup.service ] ||  rm -f "${i}"; done; \
    rm -f /lib/systemd/system/multi-user.target.wants/*; \
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/* \
    && [ -f /run/nologin ] && rm -f /run/nologin \
    && yum install -y openssh-clients openssh-server sudo python3 \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${ROCKY_USER} -u "5000" \
    && echo "${ROCKY_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${ROCKY_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${ROCKY_USER}
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/sshd", "-D", "-e"] 