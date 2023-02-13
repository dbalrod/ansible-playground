FROM alpine:3
ARG ANSIBLE_USER
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN apk update && apk add --no-cache python3 py3-pip vim openssh sshpass iputils sudo \
    && rm  -rf /tmp/* /var/cache/apk/* \
    && adduser ansible -u "5000" --disabled-password \
    && echo "$ANSIBLE_USER:$(date +%s | sha256sum | base64 | head -c 32)"|chpasswd \
    && echo "$ANSIBLE_USER ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/$ANSIBLE_USER
USER $ANSIBLE_USER
RUN mkdir -p /home/$ANSIBLE_USER/.ssh \
    && ssh-keygen -t ed25519 -f /home/$ANSIBLE_USER/.ssh/ssh_host_ed25519_key -q -N "" \
    && python3 -m pip install --no-cache-dir --user $ANSIBLE_USER \
    && pip install --no-cache-dir pywinrm pexpect==3.3
ENV PATH=$PATH:/home/$ANSIBLE_USER/.local/bin