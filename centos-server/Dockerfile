FROM centos:8
ARG CENTOS_USER
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN sed -i -e "s|mirrorlist=|#mirrorlist=|g" /etc/yum.repos.d/CentOS-* \
    && sed -i -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-* \
    && yum -y update \
    && yum install -y openssh-clients openssh-server sudo python3 epel-release \
    && yum install -y python3-pip \
    && pip3 install --no-cache-dir pexpect==3.3 \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${CENTOS_USER} -u "5000" \
    && echo "${CENTOS_USER}:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "${CENTOS_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${CENTOS_USER}
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"] 
COPY src/bin/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]