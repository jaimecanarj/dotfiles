#!/bin/sh

# Configurar monitores
xrandr --output DP-0 --primary --mode 1920x1080 --rate 165 --output HDMI-0 --mode 1920x1080 --rate 75 --right-of DP-0

# Wallpaper
feh --bg-scale ~/Imágenes/Wallpapers/Fuji\ store.jpg

# Compositor
picom &

#Ratón
xsetroot -cursor_name -left_ptr &
xset m 0 0

# Iniciar polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Iniciar notificaciones
dunst &

# Iniciar gestor portapapeles
copyq --start-server