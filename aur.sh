## Instalar AUR Helper yay

sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R jaime:jaime yay-git
cd yay-git
makepkg -si --noconfirm
cd ..
sudo rm -rf yay-git

###############################################################################
#    PAQUETES AUR                                                             #
###############################################################################

yay -S --needed --noconfirm alttab # window switcher
yay -S --needed --noconfirm code-marketplace # extensiones
yay -S --needed --noconfirm hoppscotch-bin # rest/graphql
yay -S --needed --noconfirm prismlauncher # minecraft
yay -S --needed --noconfirm losslesscut-bin # recortar vídeo
yay -S --needed --noconfirm smile # selector emoji
yay -S --needed --noconfirm anki # ssr
yay -S --needed --noconfirm eww-x11 # widgets