FROM redhat/ubi9:9.1
ARG RHEL_USER
RUN yum update \ 
    && yum install -y openssh-clients openssh-server sudo python3 \
    && yum clean all \
    && mkdir /run/sshd \
    && ssh-keygen -A \
    && adduser ${RHEL_USER} -u "5000" \
    && echo "${RHEL_USER} ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/${RHEL_USER}
CMD ["/usr/sbin/sshd", "-D", "-e"]