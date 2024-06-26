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
sudo pacman -S --needed --noconfirm calcurse # calendario
sudo pacman -S --needed --noconfirm cmus # música
sudo pacman -S --needed --noconfirm upower # datos energía dispositivo

###############################################################################
#    PAQUETES FILE EXPLORER                                                   #
###############################################################################

sudo pacman -S --needed --noconfirm thunar # explorador archivos
sudo pacman -S --needed --noconfirm gvfs # papelera
sudo pacman -S --needed --noconfirm thunar-archive-plugin # menu comprimidos
sudo pacman -S --needed --noconfirm thunar-media-tags-plugin # info media
sudo pacman -S --needed --noconfirm thunar-volman # dispositivos removibles
sudo pacman -S --needed --noconfirm tumbler # miniaturas
sudo pacman -S --needed --noconfirm ffmpegthumbnailer # miniaturas
sudo pacman -S --needed --noconfirm file-roller # compresión
sudo pacman -S --needed --noconfirm unrar # descomprimir archivos rar

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
sudo pacman -S --needed --noconfirm secrets # gestor contraseñas
sudo pacman -S --needed --noconfirm flameshot # captura de pantalla
sudo pacman -S --needed --noconfirm evince # lector pdf
sudo pacman -S --needed --noconfirm gnome-calculator # calculadora
sudo pacman -S --needed --noconfirm thunderbird # email
sudo pacman -S --needed --noconfirm rofi # menú
sudo pacman -S --needed --noconfirm pavucontrol # gestor audio
sudo pacman -S --needed --noconfirm copyq # gestor portapeles
sudo pacman -S --needed --noconfirm lxappearance # configurador tema

###############################################################################
#    PAQUETES PROGRAMACIÓN                                                    #
###############################################################################

sudo pacman -S --needed --noconfirm code # ide

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

###############################################################################
#    PAQUETES AUR                                                             #
###############################################################################

yay -S --needed --noconfirm qtile-extras # funcionalidad extra qtile
yay -S --needed --noconfirm bibata-cursor-theme-bin # tema del ratón
yay -S --needed --noconfirm code-marketplace # extensiones
yay -S --needed --noconfirm hoppscotch-bin # rest/graphql
yay -S --needed --noconfirm prismlauncher-qt5-bin # minecraft
yay -S --needed --noconfirm losslesscut-bin # recortar vídeo
yay -S --needed --noconfirm smile # selector emoji
yay -S --needed --noconfirm anki-bin # ssr
yay -S --needed --noconfirm qt5-styleplugins # tema oscuro qt

###############################################################################
#    PAQUETES LUTRIS                                                          #
###############################################################################

sudo pacman -S --needed --noconfirm wine-staging giflib lib32-giflib libpng lib32-libpng libldap lib32-libldap gnutls lib32-gnutls mpg123 lib32-mpg123 openal lib32-openal v4l-utils lib32-v4l-utils libpulse lib32-libpulse libgpg-error lib32-libgpg-error alsa-plugins lib32-alsa-plugins alsa-lib lib32-alsa-lib libjpeg-turbo lib32-libjpeg-turbo sqlite lib32-sqlite libxcomposite lib32-libxcomposite libxinerama lib32-libgcrypt libgcrypt lib32-libxinerama ncurses lib32-ncurses ocl-icd lib32-ocl-icd libxslt lib32-libxslt libva lib32-libva gtk3 lib32-gtk3 gst-plugins-base-libs lib32-gst-plugins-base-libs vulkan-icd-loader lib32-vulkan-icd-loader