#!/bin/bash

if [[ "${UID}" != "0" ]]; then
    echo "PLZ run as root"
    exit 1
fi

yum install -y iptables-services

echo 'Now shutting down firewall and SElinux'
systemctl stop firewalld && systemctl disable firewalld

iptables -F && iptables -Z && iptables -X

SETATUS=$(more /etc/selinux/config | sed -n 7p | awk -F "=" '{print $NF}')

if [[ "{$SESTATUS}" != "disabled" ]]; then
    setenforce 0
fi

wget -v https://mirrors.tuna.tsinghua.edu.cn/mysql/yum/mysql-8.0-community-el7-x86_64/mysql80-community-release-el7-11.noarch.rpm

yum -y localinstall ./mysql80-community-release-el7-11.noarch.rpm

sed 's/gpgcheck=1/gpgcheck=0/g' /etc/yum.repos.d/mysql-community.repo

yum clean all

yum install -y mysql-community-server

systemctl enable mysqld && systemctl start mysqld

echo "skip-grant-tables" >> /etc/my.cnf
