#!/bin/bash 


#Tools INSTALLERv1

#By LzMuxIts.17

#Baru pertama Buat Cok jangan di bully

#Thanks to MA.Imam Syafi'i 

clear

red='\e[;34m'
blue='\e[;39m'
green='\e[36m'
okgreen'\33[92m'
white'\[1;37m'
lhitgreen'\[1;32m'
cyan'\[1;37m'


================================================
#CTRL C
================================================

trap ctrl_c INT
ctrl_c() {
clear
  
echo  - e  $ red '[#]> (CTRL + C) Jika Ingin Keluar blue 
 
sleep 1
  echo ""
  
echo -e $blue'[#]> By LzMuxIts.17 and You $red. 
  
 sleep 1
  echo ""
  
  echo -e $red'[#]> Baru Pertama Buat Cok ! $blue 
  
  sleep 1
  echo ""
  
  echo -e $yellow'[#]> Thanks For Visited All
  
  sleep 1
  echo ""
  
  echo -e $yellow'[#]> Thanks For MA.Imam Syafi'i
  
  read enter
  clear
  
  }

  echo -e $yellow".  Termux.ID.    $green  #"
  echo  - e  $red"INSTALLERTOOLS.v1. $white. #"
  echo -e $white"   Conntac-me LzMuxIts.17@gmail.com  $green #"
  echo -e $yellow". By LzMuxIts amd You.  $white #"
  echo -e $purple". thanks to HACKER'S KATROK_LOL  $red  #"
  echo ""
  echo -e $yellow 01. wedav"
  echo -e $yellow 02. red-hawk"
  echo -e $yellow 03. gmail brute force"
  echo -e $yellow 04. Ip-geolocation"
  echo -e $yellow 05. boot aouto deface"
  echo -e $yellow 06. katollin"
  echo -e $yellow 07. Hydra"
  echo -e $yellow 08. SQLmap"
  echo -e $yellow 09. FBbrute"
  echo -e $yellow 10. torshammer"
  echo -e $yellow 11. instaboot"
  echo -e $yellow 12. admin finder"
  echo -e $yellow 13. Hunner"
  echo -e $yellow 14. sudo"
  echo -e $yellow 15. ngrok"
  echo -e $yelloe 00. Exit 
  echo -e $red""
read -p "[LzMuxIts.17]> " act;


  if [ $act = 01 ] || [ $act = 01 ]
then
clear
echo -e $yellow" installing webdav "
sleep 1 
apt update && apt upgrade
apt install python
apt-get install python-pip
pip2 install urllib3 chardet certifi idna requests
apt install openssl curl
pkg install libcurl
mkdir webdav
cd ~/webdav
wget https://pastebin.com/raw/HnVyQPtR -O webdav.py
chmod 777 webdav.py
cd ~/
sleep 1
echo -e $pink" Mantap Cok "
fi

if [ $act = 02 ] || [ $act = 02 ]
then
clear
echo -e $yellow"installing red-hawk "
sleep 1
apt update && apt upgrade
apt install php
apt install git
git clone https://github.com/Tuhinshubhra/RED_HAWK
sleep 1
  echo -e $pink" Mantap Cok "
fi

if [ $act = 03 ] || [ $act = 03 ]
then
clear
echo -e $yellow" installing gmail brute force "
sleep 1
apt-get update && apt-get upgrade
apt-get install git
git clone https://github.com/JamesAndresCM/Brute_force_gmail
sleep 1
echo -e $pink" Usage: python2.7 brute_force_gmail.py Ngentot170@gmail.com PATH_TO_DICTIONARY "
fi

if [ $act = 04 ] || [ $act = 04 ]
then
clear
echo -e $yellow" installing Ip-geolocation "
sleep 1
apt-get update && apt-get upgrade
apt-get install git
apt install python
git clone https://github.com/maldevel/IPGeolocation.git
cd IPGeolocation
chmod +x ipgeolocation.py
pip install -r requirements.txt
sleep 1
echo -e $yellow" Mantap Cok "
fi

if [ $act = 05 ] || [ $act = 05 ]
then
clear
echo -e $yellow" installing boot auto deface "
sleep 1 
apt-get update && apt-get upgrade
apt-get install git 
apt-get install wget 
apt-get install perl 
apt-get install unzip
git clone https://github.com/mrcakil/bot.git
cd bot
unzip bot.zip
chmod 777 bot.pl
echo -e $pink" Lokasi bot ? /bot/bot.pl"
echo -e $pink" Mantap Cok "
fi

if [ $act = 06 ] || [ $act = 06 ]
then
clear
echo -e $yellow" installing katoolin "
sleep 1
apt update && apt upgrade
pkg install git
pkg install python
pkg install gnupg
pkg install nano
git clone https://github.com/LionSec/katoolin.git
cd ~/katoolin
echo -e $red"note :  nano katoolin.py 
ganti semua kode /etc/apt/source.list dengan /data/data/com.termux/files/usr/etc/apt/sources.list 
kemudian simpan dengan menekan ctrl O enter kemudian ctrl X . 
jika tidak ada menu ctrl pada keyboard munculkan dengan menahan tombol volume atas kemudian ketik Q pada keyboard maka menu ctrl akan muncul di atas keyboard
python2 katoolin.py
Sisanya bisa mengikuti cara install di atas, Jika menemui masalah gpg error saat melakukan add repository install gnupg-curl dengan perintah pkg install gnupg-curl
Untuk yg menggunakan termux dengan cpu arm64 (aarch64) tidak bisa menambahkan repositori kali linux karna kali linux tidak support aarch64, 
jadi sebelum menginstall tools kali di termux wajib dengan android dengan arm32 jika arm64 gunakan gnuroot"
echo -e $yellow" Mantap Cok "
fi

if [ $act = 07 ] || [ $act = 07 ]
then
clear
echo -e $yellow" installing Hydra "
sleep 1
apt update && apt install -y wget
apt install hydra
wget http://scrapmaker.com/download/data/wordlists/dictionaries/rockyou.txt
cd ~/
echo -e $pink" Mantap Cok "
fi

if [ $act = 08 ] || [ $act = 08 ]
then
clear
echo -e $yellow" installing SQLmap "
sleep 1
apt update && apt upgrade
apt install python2
git clone https://github.com/sqlmapproject/sqlmap.git
cd ~/
echo -e $pink" Mantap Cok "
fi

if [ $act = 09 ] || [ $act = 09 ]
then
clear
echo -e $yellow" installing FBbrute "
sleep 1
apt install python2
apt install python2-dev
apt install wget
pip2 install mechanize
mkdir fbbrute
cd ~/fbbrute
wget https://pastebin.com/raw/aqMBt2xA -O fbbrute.py
wget http://override.waper.co/files/password.apk -O wordlist.txt
chmod 777 fbbrute.py
cd ~/
echo -e $pink" Mantap Cok "
fi

if [ $act = 10 ] || [ $act = 10 ]
then
clear
echo -e $yellow" installing torshammer "
sleep 1
pkg update
pkg upgrade
pkg install python
pkg install git
git clone https://github.com/cyweb/hammer
cd ~/
echo -e $pink" Mantap Cok "
fi

if [ $act = 11 ] || [ $act = 11 ]
then
clear
echo -e $yellow" installing Instabot instagram bot "
sleep 1
apt-get update && apt-get upgrade
pkg install python
apt-get install git
apt-get install nano
git clone https://github.com/instabot-py/instabot.py
echo -e $pink" Mantap Cok "
echo -e $pink" waiting itu sakit Cok. "
echo -e $pink" Waiting itu sakit Cok. "
fi

if [ $act = 12 ] || [ $act = 12 ]
then
clear
echo -e $yellow" Installing admin finder "
sleep 1
apt update && apt upgrade
apt-get install php
mkdir adfin
cd ~/webdav
wget https://pastebin.com/raw/32txZ6Qr -O adfin.php
cd ~/
echo -e $yellow" Mantap Cok "
fi

if [ $act = 13 ] || [ $act = 13 ]
then
clear
echo -e $yellow" Installing Hunner "
sleep 1
apt-get update && apt-get upgrade
apt install python
apt install git
git clone https://github.com/b3-v3r/Hunner
echo -e $pink" Mantap Cok "
fi

if [ $act = 14 ] || [ $act = 14 ]
then
clear
echo -e $yellow" installing sudo "
sleep 1
apt update && apt upgrade
pkg install git ncurses-utils
git clone https://github.com/st42/termux-sudo.git
cd termux-sudo
cat sudo > /data/data/com.termux/files/usr/bin/sudo
chmod 700 /data/data/com.termux/files/usr/bin/sudo
echo -e $pink" Mantap Cok "
fi

if [ $act = 15 ] || [ $act = 15 ]
then
clear
echo -e $yellow" Installing Ngrok "
sleep 1
apt install wget
mkdir ngrok
cd ~/ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
cd ~/
echo -e $pink" Mantap Cok "
fi

if [ $act = 55 ] || [ $act = 55 ]
then
echo -e $yellow" Maafin cuma segini "
sleep 1
echo -e $yellow" baru belajar buat "
sleep 1
echo -e $green" jan lupa sholatnya Cok "
sleep 1
echo -e $green" soory kasar anjing "
sleep 1
echo -e $green" contact : LzMuxIts.17@gmail.com "
sleep 1
echo -e $red" ngopi Cok "
sleep 1
echo -e $red" dadah :* "
sleep 1
exit
fi









