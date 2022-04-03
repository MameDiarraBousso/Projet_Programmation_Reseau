#!/bin/bash
sudo apt -y install dnsutils
sudo apt -y install wget
wget https://github.com/iredmail/iRedMail/archive/1.5.2.tar.gz
tar xvf 1.5.2.tar.gz
chmod +x /root/iRedMail-1-5-2/iRedmail-1-5-2.sh
./iRedMail-1-5-2/iRedMail-1-5-2.sh
