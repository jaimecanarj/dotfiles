#!/bin/bash

###############################################################################
#    PAQUETES BÁSICOS                                                         #
###############################################################################

sudo pacman -S --needed --noconfirm qtile # window manager
sudo pacman -S --needed --noconfirm python-dbus-next # window manager
sudo pacman -S --needed --noconfirm lightdm # display-manager
sudo pacman -S --needed --noconfirm lightdm-webkit2-greeter # greeter
sudo pacman -S --needed --noconfirm xorg-xrandr # xrandr
sudo pacman -S --needed --noconfirm xorg-xsetroot # ratón
sudo pacman -S --needed --noconfirm pacman-contrib # checkupdates
sudo pacman -S --needed --noconfirm rebuild-detector # checkrebuild
sudo pacman -S --needed --noconfirm reflector # actualizar mirrors
sudo pacman -S --needed --noconfirm ufw # firewall
sudo pacman -S --needed --noconfirm picom # compositor
sudo pacman -S --needed --noconfirm feh # wallpaper
sudo pacman -S --needed --noconfirm dunst # notificaciones
sudo pacman -S --needed --noconfirm ntfs-3g # montar discos ntfs
sudo pacman -S --needed --noconfirm alsa-utils # sonido
sudo pacman -S --needed --noconfirm playerctl # sonido
sudo pacman -S --needed --noconfirm git # gestor versiones
sudo pacman -S --needed --noconfirm bluez # bluetooth
sudo pacman -S --needed --noconfirm bluez-utils # bluetooth
sudo pacman -S --needed --noconfirm blueman # bluetooth
sudo pacman -S --needed --noconfirm polkit-gnome # polkit
sudo pacman -S --needed --noconfirm gtk-engine-murrine # temas gtk
sudo pacman -S --needed --noconfirm gtk-themes-extra # temas gtk
sudo pacman -S --needed --noconfirm qt5ct # temas qt

###############################################################################
#    PAQUETES TERMINAL                                                        #
###############################################################################

sudo pacman -S --needed --noconfirm kitty # terminal
sudo pacman -S --needed --noconfirm btop # monitor recursos
sudo pacman -S --needed --noconfirm neofetch # datos sistema
sudo pacman -S --needed --noconfirm neovim # editor texto
sudo pacman -S --needed --noconfirm bat # alternativa a cat
sudo pacman -S --needed --noconfirm eza # alternativa a ls
sudo pacman -S --needed --noconfirm gdu # gestor de disco
sudo pacman -S --needed --noconfirm upower # datos energía dispositivo
sudo pacman -S --needed --noconfirm yazi # explorador de archivos

###############################################################################
#    PAQUETES FILE EXPLORER                                                   #
###############################################################################

sudo pacman -S --needed --noconfirm nautilus # explorador archivos
sudo pacman -S --needed --noconfirm file-roller # compresión
sudo pacman -S --needed --noconfirm gnome-disk-utility # montar imágenes iso
sudo pacman -S --needed --noconfirm tumbler # miniaturas
sudo pacman -S --needed --noconfirm ffmpegthumbnailer # miniaturas
sudo pacman -S --needed --noconfirm gvfs-mtp # montar dispositivos moviles

###############################################################################
#    PAQUETES FUENTES                                                         #
###############################################################################

sudo pacman -S --needed --noconfirm noto-fonts # fuentes básicas
sudo pacman -S --needed --noconfirm ttf-liberation # fuentes metric-compatible
sudo pacman -S --needed --noconfirm ttf-jetbrains-mono-nerd # fuente mono
sudo pacman -S --needed --noconfirm noto-fonts-cjk # fuentes japonesas
sudo pacman -S --needed --noconfirm noto-fonts-emoji # emojis

###############################################################################
#    PAQUETES PROGRAMAS BÁSICOS                                               #
###############################################################################

sudo pacman -S --needed --noconfirm firefox # navegador web
sudo pacman -S --needed --noconfirm vlc # video
sudo pacman -S --needed --noconfirm eog # visor imágenes
sudo pacman -S --needed --noconfirm krita # editor imágenes
sudo pacman -S --needed --noconfirm secrets # gestor contraseñas
sudo pacman -S --needed --noconfirm flameshot # captura de pantalla
sudo pacman -S --needed --noconfirm evince # lector pdf
sudo pacman -S --needed --noconfirm gnome-calculator # calculadora
sudo pacman -S --needed --noconfirm gnome-music # música
sudo pacman -S --needed --noconfirm gnome-calendar # calendario
sudo pacman -S --needed --noconfirm rofi # menú
sudo pacman -S --needed --noconfirm pavucontrol # gestor audio
sudo pacman -S --needed --noconfirm copyq # gestor portapeles
sudo pacman -S --needed --noconfirm lxappearance # configurador tema

###############################################################################
#    PAQUETES JUEGOS                                                          #
###############################################################################

sudo pacman -S --needed --noconfirm lib32-nvidia-utils # vulkan
sudo pacman -S --needed --noconfirm steam # juegos
sudo pacman -S --needed --noconfirm lutris # wine
sudo pacman -S --needed --noconfirm gamemode # daemon rendimiento
sudo pacman -S --needed --noconfirm mangohud # overlay rendimiento
sudo pacman -S --needed --noconfirm lib32-mangohud # overlay rendimiento

###############################################################################
#    PAQUETES MISCELÁNEA                                                      #
###############################################################################

sudo pacman -S --needed --noconfirm amule # transferencia p2p
sudo pacman -S --needed --noconfirm aria2 # transferencia p2p
sudo pacman -S --needed --noconfirm discord # comunicación
sudo pacman -S --needed --noconfirm picard # editar etiquetas música
sudo pacman -S --needed --noconfirm gnome-boxes # máquinas virtuales
sudo pacman -S --needed --noconfirm github-cli # github

###############################################################################
#    PAQUETES PROGRAMACIÓN                                                    #
###############################################################################

sudo pacman -S --needed --noconfirm php #php
sudo pacman -S --needed --noconfirm php-apache #php
sudo pacman -S --needed --noconfirm composer #composer
sudo pacman -S --needed --noconfirm mariadb #mariadb
sudo pacman -S --needed --noconfirm nodejs #node
sudo pacman -S --needed --noconfirm npm #npm

###############################################################################
#    PAQUETES AUR                                                             #
###############################################################################

yay -S --needed --noconfirm telegram-desktop-bin # telegram
yay -S --needed --noconfirm qtile-extras # funcionalidad extra qtile
yay -S --needed --noconfirm bibata-cursor-theme-bin # tema del ratón
yay -S --needed --noconfirm phpstorm # ide
yay -S --needed --noconfirm phpstorm-jre # ide
yay -S --needed --noconfirm prismlauncher-qt5-bin # minecraft
yay -S --needed --noconfirm losslesscut-bin # recortar vídeo
yay -S --needed --noconfirm smile # selector emoji
yay -S --needed --noconfirm qt5-styleplugins # tema oscuro qt
yay -S --needed --noconfirm onlyoffice-bin # office

###############################################################################
#    PAQUETES LUTRIS                                                          #
###############################################################################

sudo pacman -S --needed --noconfirm wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses ocl-icd lib32-ocl-icd libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader
