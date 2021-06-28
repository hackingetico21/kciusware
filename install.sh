#! /usr/bin/bash
null="> /dev/null 2>&1"
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo -e $b">"$w" KCIUSWARE es un ataque basico Ransomware para Android"
echo -e $b">"$w" preparado para instalar dependencias ..."
sleep 3
echo -e $b">"$w" instalando paquete: "$g"default-jdk"$w
sudo apt-get install default-jdk -y
echo -e $b">"$w" instalando paquete: "$g"aapt"$w
sudo apt-get install aapt zipalign -y
echo -e $b">"$w" instalando paquete: "$g"apktool"$w
sudo apt-get install apktool -y
echo -e $b">"$w" instalando paquete: "$g"imagemagick"$w
sudo apt-get install imagemagick -y
echo -e $b">"$w" instalando paquete: "$g"python3"$w
sudo apt-get install python3 python3-pip -y
echo -e $b">"$w" instalando modulos: "$g"pillow"$w
pip3 install Pillow
echo -e $b">"$w" dependencias instaladas"
echo -e $b">"$w" use el comando "$g"python3 kciusware.py"$w" para iniciar la consola"
