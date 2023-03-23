FROM redhat/ubi9:9.1
ARG RHEL_USER
RUN yum update \ 
    && yum install -y openssh-clients openssh-server sudo python3 python3-pip \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${RHEL_USER} -u "5000" \
    && echo "${RHEL_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${RHEL_USER}
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"] 
COPY src/bin/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]