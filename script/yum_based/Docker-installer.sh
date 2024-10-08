#!/bin/bash

# Docker installer for CentOS7.9

yum remove -y docker \
 docker-client \
 docker-client-latest \
 docker-common \
 docker-latest \
 docker-latest-logrotate \
 docker-logrotate \
 docker-engine


yum install -y yum-utils \
 device-mapper-persistent-data \
 lvm2

yum-config-manager --add-repo \
 https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

systemctl start docker
