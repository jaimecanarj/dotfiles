#!/bin/sh

# Wallpaper
feh --bg-scale ~/Imágenes/Wallpapers/cgrdi4O.png

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

# Desactivar salvador de pantalla
xset s off
xset -dpms