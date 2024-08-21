rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org

yum install -y https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm

yum --enablerepo=elrepo-kernel list available


yum --enablerepo=elrepo-kernel install kernel-lt -y


grub2-set-default 0 && grub2-mkconfig -o /etc/grub2.cfg