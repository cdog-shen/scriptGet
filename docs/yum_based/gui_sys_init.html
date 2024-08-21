#!/bin/bash
##############################################
#Description : Linux System initialize script
#Author      : cdog/shencdog@gmail.com
#Date        : 2024-03-07
#Version     : 1.0
##############################################


#------const start------

# window size
HEI=40
WID=70


#packages
GUI_PACK="dialog"
TOOL_PACK_LIST="git vim  net-tools openssl \
bridge-* wget curl gcc make telnet apr* lsof pcre*  \
sqlite-devel prel*"
DEPENDENCE_PACK_LIST="libxml2*"

#status
STATUS_SELINUX=$(getenforce | awk '{ if ($1 = 0) {print "enable" } else { print "disabled" } }')
STATUS_FIREWALL=$(systemctl status firewalld | grep "Active" | awk -F':' '{ print $2 }')
STATUS_SSHD=$(systemctl status sshd | grep "Active" | awk -F':' '{ print $2 }')
IPADDRS=$(ip addr show | grep 'inet ' | awk '{print $2}' | grep -v '127')
NETIFS=$(ip a | grep "state UP" | grep -v "LOOPBACK" | awk -F':'  '{print $2}')
DNS=$(cat '/etc/resolv.conf' | grep "name" | awk -F" " '{ print $2 }')

#file PATH
PATH_ISO='/root/rocky-install.iso'

#------const end------


#------function start------

GUI_SYS_STUTUS() {
    dialog --title "Linux System initialize script --- System status" --msgbox "

    Hostname = $HOSTNAME

    UP Time = $(uptime)

    SELinux status = $STATUS_SELINUX

    Firewall status = $STATUS_FIREWALL

    SSH server status = $STATUS_SSHD

    NetWork status = "OK"

            Interfaces = $NETIFS

            IPs = $IPADDRS

            DNS server = $DNS

    " $HEI $WID
}

GEN_LO_REPO_FILE(){
    echo '[cd-media-AppStream]' > /etc/yum.repos.d/localRepo.repo
    echo 'name=AppStream' >> /etc/yum.repos.d/localRepo.repo
    echo 'baseurl=file:///repo/AppStream' >> /etc/yum.repos.d/localRepo.repo
    echo 'gpgcheck=0' >> /etc/yum.repos.d/localRepo.repo
    echo 'enabled=1' >> /etc/yum.repos.d/localRepo.repo
    echo "" >> /etc/yum.repos.d/localRepo.repo
    echo '[cd-media-BaseOS]' >> /etc/yum.repos.d/localRepo.repo
    echo 'name=BaseOS' >> /etc/yum.repos.d/localRepo.repo
    echo 'baseurl=file:///repo/BaseOS' >> /etc/yum.repos.d/localRepo.repo
    echo 'gpgcheck=0' >> /etc/yum.repos.d/localRepo.repo
    echo 'enabled=1' >> /etc/yum.repos.d/localRepo.repo
}

GEN_IF_FILE(){
    F_PATH="/etc/NetworkManager/system-connections/$1.nmconnection"
    echo '[connection]' > $F_PATH
    echo "id=$1" >> $F_PATH
    echo 'type=ethernet' >> $F_PATH
    echo 'autoconnect-priority=-999' >> $F_PATH
    echo "interface-name=$1" >> $F_PATH

    echo '[ethernet]' >> $F_PATH

    echo '[ipv4]' >> $F_PATH
    echo "address1=" >> $F_PATH
    echo "dns=;" >> $F_PATH
    echo 'method=manual' >> $F_PATH

    echo '[ipv6]' >> $F_PATH
    echo 'addr-gen-mode=eui64' >> $F_PATH
    echo 'method=auto' >> $F_PATH

    echo '[proxy]' >> $F_PATH

}



#------function end------



if [ "${UID}" != "0" ];then
	echo "=================="
	echo -e "Must Be To root"
	echo "=================="
	exit 1
fi 

while true; do

    echo "Now testing network connection..."

    ping baidu.com -c 2 > /dev/null 2>&1

    if [ "$?" != "0" ]; then
        while true; do
            read -rep 'Network Err, Do you want to config it now? (y/N):' -i "N" answer
            if [ "$answer" == "N" ]; then
                echo 'user abort. Exiting shell...'
                exit 1
            fi
            echo "Your interfaces is : $NETIFS"
            read -rep "Choice one you want to config : " -i "ens160" interface
            read -rep "Type your IPADDR : " -i "" ipaddr
            read -rep "Your PREFIX lenth : " -i "24" prefix_length

            ip addr add "$ipaddr/$prefix_length" dev "$interface" 2 > /dev/null 2>&1

            if [ "$?" != "0" ]; then
                break
            fi

            echo "ip config failure, check your input ?"

        done
    else
        break
    fi
done

yum install -y $GUI_PACK && echo "Start GUI interface..."

# read -rep "a pause"

GUI_SYS_STUTUS

while true; do

    CHOICE=$(dialog --title "Linux System initialize script --- Main Menu" \
        --menu "Choose one (Cancel is EXIT !!!)" $HEI $WID 10\
        1 "Change Hostname..." \
        2 "Modify network setting..." \
        3 "Set local repo" \
        4 "Recover online repo" \
        5 "Install recommendation packages" \
        0 "System status" \
        2>&1 >/dev/tty)

    case $CHOICE in
        1)
            USER_HOSTNAME=$(dialog --title "Hostname config" \
            --inputbox "input your hostname PLZ :" \
            10 30 2>&1 >/dev/tty)
            if [ "${USER_HOSTNAME}" == "" ]; then
                dialog --msgbox "Did you input anything ?" 5 40 
                continue
            fi
            hostnamectl set-hostname $USER_HOSTNAME
            if [ "$?" != "0" ]; then
                dialog --msgbox "Hostname set failure. Check your input" 5 45
                continue
            fi
            # for test
            # echo $USER_HOSTNAME
            # exit 0 
            ;;

        2)
            C_IFACE=$(dialog --title "InterFace select" \
            --inputbox "input your interface name :" 10 30 \
            2>&1 >/dev/tty)
            echo $NETIFS | grep $C_IFACE
            if [ "$?" == "1" ]; then
                dialog --title "confirm?" \
                --yesno "the interface you select seems not a physical interface, would you like to continue ?" \
                10 30 
                if [ "$?" != 0 ]; then
                    continue
                fi
                GEN_IF_FILE "$C_IFACE"
            fi
            T_IPADDR=$(dialog --title "InterFace config" \
            --inputbox "input your interface ip addr :" 10 30 \
            2>&1 >/dev/tty)
            T_PREFIX=$(dialog --title "InterFace config" \
            --inputbox "input your interface prefix lenth :" 10 30 \
            2>&1 >/dev/tty)
            T_GW=$(dialog --title "InterFace config" \
            --inputbox "input your interface gatewat addr :" 10 30 \
            2>&1 >/dev/tty)
            T_DNS=$(dialog --title "InterFace config" \
            --inputbox "input your interface dns addr :" 10 30 \
            2>&1 >/dev/tty)
            #catch
            TEMP=$(grep "address1" "/etc/NetworkManager/system-connections/$C_IFACE.nmconnection")
            sed -i "s#$TEMP#address1=$T_IPADDR/$T_PREFIX,$T_GW#g" "/etc/NetworkManager/system-connections/$C_IFACE.nmconnection"
            TEMP=$(grep "dns" "/etc/NetworkManager/system-connections/$C_IFACE.nmconnection")
            sed -i "s#$TEMP#dns=$T_DNS;#g"
            ;;

        3)
            mkdir /repo
            M_MODE=$(dialog --title "Repo Mod select" \
            --menu "Choose one (Cancel is EXIT !!!)" 20 $WID 2\
            1 "Use CD ROM" \
            2 "Use ISO file" \
            2>&1 >/dev/tty)
            case $M_MODE in
                1)
                mount /dev/cdrom /repo
                ;;

                2)
                mount $PATH_ISO /repo -o loop
                ;;

                *)
                continue
                ;;
            esac

            if [ -z "$(ls -A /repo)" ]; then
                dialog --msgbox "mount Failure. Check your setting..." 10 20
                continue
            fi

            mkdir /etc/yum.repos.d/bak
            mv /etc/yum.repos.d/*.* /etc/yum.repos.d/bak
            GEN_LO_REPO_FILE
            ;;

        4)
            rm -f /etc/yum.repos.d/localRepo.repo
            mv /etc/yum.repos.d/bak/* /etc/yum.repos.d
            dialog --msgbox "OK" 5 10
            ;;

        5)
            yum install -y $TOOL_PACK_LIST $DEPENDENCE_PACK_LIST
            ;;

        0)
            GUI_SYS_STUTUS
            ;;
    
        *)
            dialog --msgbox "Bey~" 5 10
            break
    esac
done
