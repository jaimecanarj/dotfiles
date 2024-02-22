#!/bin/bash

###############################################################################
#    CONFIGURAR SISTEMA                                                       #
###############################################################################

## Configurar firewall

sudo systemctl enable ufw.service --now # activar firewall
sudo ufw allow 80/tcp # permitir tráfico http
sudo ufw allow 443/tcp # permitir tráfico https
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable

## Configurar mirrors

sudo systemctl enable reflector.timer

## Ajutar hora reloj linux-windows

sudo timedatectl set-local-rtc 1 --adjust-system-clock

###############################################################################
#    PERSONALIZAR SISTEMA                                                     #
###############################################################################

cp .Xresources ~/ # Configurar ratón
mkdir ~/.local/share/icons # Crear carpeta tema iconos
tar -xf TokyoNight-SE.tar.bz2 -C ~/.local/share/icons/ # Extraer tema iconos 
mkdir ~/.themes # Crear carpeta tema gtk
unzip Tokyonight-Dark-BL.zip -d ~/.themes # Extraer tema gtk
cp -r .config/* ~/.config/