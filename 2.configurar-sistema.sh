#!/bin/bash

###############################################################################
#    CONFIGURAR SISTEMA                                                       #
###############################################################################

# Configurar display manager
sudo systemctl enable lightdm.service
sudo cp lightdm/lightdm.conf /etc/lightdm/lightdm.conf
sudo cp lightdm/lightdm-webkit2-greeter.conf /etc/lightdm/lightdm-webkit2-greeter.conf
sudo cp -r lightdm/tokyonight /usr/share/lightdm-webkit/themes/

# Configurar firewall

sudo systemctl enable ufw.service --now # activar firewall
sudo ufw allow 80/tcp # permitir tráfico http
sudo ufw allow 443/tcp # permitir tráfico https
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable

# Configurar mirrors

sudo systemctl enable reflector.timer

# Ajustar hora reloj linux-windows

sudo timedatectl set-local-rtc 1 --adjust-system-clock

# Configurar bluetooth
sudo systemctl enable bluetooth

# Configurar gvfs para no automontar
sudo cp ./mtp.mount /usr/share/gvfs/mounts/mtp.mount

###############################################################################
#    PERSONALIZAR SISTEMA                                                     #
###############################################################################

cp .Xresources ~/ # Configurar ratón
mkdir ~/.local/share/icons # Crear carpeta tema iconos
tar -xf TokyoNight-SE.tar.bz2 -C ~/.local/share/icons/ # Extraer tema iconos 
mkdir ~/.themes # Crear carpeta tema gtk
unzip Tokyonight-Dark-BL.zip -d ~/.themes # Extraer tema gtk
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim #Instalar NvChad
cp -r .config/* ~/.config/ # Copiar archivos de configuración
cp -r .local/* ~/.local/ # Copiar archivos de configuración
bat cache --build # Actualizar temas de bat
