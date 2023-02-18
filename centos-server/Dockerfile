FROM centos:7
ARG CENTOS_USER
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
    && yum install -y openssh-clients openssh-server sudo python2 epel-release \
    && yum update -y \
    && yum install -y python-pip \
    && pip2 install --no-cache-dir pexpect==3.3 \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${CENTOS_USER} -u "5000" \
    && echo "${CENTOS_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${CENTOS_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${CENTOS_USER}
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/sshd", "-D", "-e"] 