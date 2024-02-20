#!/bin/bash

###############################################################################
#    PAQUETES BÁSICOS                                                         #
###############################################################################

sudo pacman -S --needed --noconfirm xorg-xrandr # xrandr
sudo pacman -S --needed --noconfirm pacman-contrib # checkupdates
sudo pacman -S --needed --noconfirm rebuild-detector # checkrebuild
sudo pacman -S --needed --noconfirm reflector # mirrors utility
sudo pacman -S --needed --noconfirm ufw # firewall
sudo pacman -S --needed --noconfirm picom # compositor
sudo pacman -S --needed --noconfirm feh # wallpaper/image viewer
sudo pacman -S --needed --noconfirm dunst # notifications
sudo pacman -S --needed --noconfirm ntfs-3g # ntfs disk mount
sudo pacman -S --needed --noconfirm alsa-utils # sonido
sudo pacman -S --needed --noconfirm playerctl # sonido
sudo pacman -S --needed --noconfirm git # gestor versiones
sudo pacman -S --needed --noconfirm bluez # bluetooth
sudo pacman -S --needed --noconfirm bluez-utils # bluetooth
sudo pacman -S --needed --noconfirm blueman # bluetooth
sudo pacman -S --needed --noconfirm polkit-gnome # polkit

###############################################################################
#    CONFIGURAR SISTEMA                                                       #
###############################################################################

## Cofigurar pacman

mv pacman.conf /etc/pacman.conf

## Configurar firewall

sudo systemctl enable ufw.service --now # activar firewall
sudo ufw allow 80/tcp # permitir tráfico http
sudo ufw allow 443/tcp # permitir tráfico https
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable

## Configurar mirrors

sudo systemctl enable reflector.timer

## Instalar AUR Helper yay

sudo git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si
cd ..
rm -rf yay-git

## Ajutar hora reloj linux-windows

timedatectl set-local-rtc 1 --adjust-system-clock

###############################################################################
#    PAQUETES TERMINAL                                                        #
###############################################################################

sudo pacman -S --needed --noconfirm kitty # terminal
sudo pacman -S --needed --noconfirm btop # resource monitor
sudo pacman -S --needed --noconfirm neofetch # system stats
sudo pacman -S --needed --noconfirm neovim # text editor
sudo pacman -S --needed --noconfirm bat # cat alternative
sudo pacman -S --needed --noconfirm exa # ls alternative
sudo pacman -S --needed --noconfirm gdu # gestor de disco
sudo pacman -S --needed --noconfirm calcurse # calendario

###############################################################################
#    PAQUETES FILE EXPLORER                                                   #
###############################################################################

sudo pacman -S --needed --noconfirm thunar # file explorer
sudo pacman -S --needed --noconfirm gvfs # papelera
sudo pacman -S --needed --noconfirm thunar-archive-plugin # menu contextual
sudo pacman -S --needed --noconfirm thunar-media-tags-plugin # media info
sudo pacman -S --needed --noconfirm thunar-volman # dispositivos removibles
sudo pacman -S --needed --noconfirm tumbler # miniaturas
sudo pacman -S --needed --noconfirm ffmpegthumbnailer # miniaturas
sudo pacman -S --needed --noconfirm file-roller # compresión
sudo pacman -S --needed --noconfirm unrar # descomprimir archivos rar

###############################################################################
#    PAQUETES FUENTES                                                         #
###############################################################################

sudo pacman -S --needed --noconfirm noto-fonts # fuentes básicas
sudo pacman -S --needed --noconfirm noto-fonts-cjk # fuentes japonesas
sudo pacman -S --needed --noconfirm noto-fonts-emoji # emojis

###############################################################################
#    PAQUETES PROGRAMAS BÁSICOS                                               #
###############################################################################

sudo pacman -S --needed --noconfirm firefox # web browser
sudo pacman -S --needed --noconfirm vlc # video
sudo pacman -S --needed --noconfirm cmus # música
sudo pacman -S --needed --noconfirm secrets # password manager
sudo pacman -S --needed --noconfirm flameshot # captura de pantalla
sudo pacman -S --needed --noconfirm mupdf # pdf reader
sudo pacman -S --needed --noconfirm gnome-calculator # calculadora
sudo pacman -S --needed --noconfirm thunderbird # email
sudo pacman -S --needed --noconfirm rofi # menú
sudo pacman -S --needed --noconfirm pavucontrol # audio manager
sudo pacman -S --needed --noconfirm gpaste # clipboard manager
sudo pacman -S --needed --noconfirm lxappearance # theme settings
yay -S --needed --noconfirm alttab # window switcher

###############################################################################
#    PAQUETES PROGRAMACIÓN                                                    #
###############################################################################

sudo pacman -S --needed --noconfirm code # ide
yay -S --needed --noconfirm code-marketplace # extensiones
yay -S --needed --noconfirm hoppscotch-bin # rest/graphql

###############################################################################
#    PAQUETES JUEGOS                                                          #
###############################################################################

sudo pacman -S --needed --noconfirm steam # juegos
sudo pacman -S --needed --noconfirm lutris # wine
yay -S --needed --noconfirm prismlauncher # minecraft

###############################################################################
#    PAQUETES MISCELÁNEA                                                      #
###############################################################################

sudo pacman -S --needed --noconfirm amule # transferencia p2p
sudo pacman -S --needed --noconfirm aria2c # transferencia p2p
sudo pacman -S --needed --noconfirm discord # comunicación
sudo pacman -S --needed --noconfirm picard # tag edit
sudo pacman -S --needed --noconfirm anki # ssr
sudo pacman -S --needed --noconfirm upower # datos energía dispositivo
sudo pacman -S --needed --noconfirm gnome-boxes # máquinas virtuales
yay -S --needed --noconfirm losslesscut-bin # recortar vídeo
yay -S --needed --noconfirm smile # selector emoji
yay -S --needed --noconfirm eww-x11 # widgets


