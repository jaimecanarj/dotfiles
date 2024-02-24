#!/bin/sh

# Configurar monitores
xrandr --output DP-0 --primary --mode 1920x1080 --rate 165 --output HDMI-0 --mode 1920x1080 --rate 75 --right-of DP-0

# Wallpaper
feh --bg-scale ~/Wallpapers/Fuji\ store.jpg

# Compositor
picom & #

#Ratón
xsetroot -cursor_name -left_ptr &
xset m 0 0

#Alt tab
alttab -bg "#1a1b26" -fg "#a9b1d6" -frame "#7aa2f7" -inact "#1a1b26" &

# Iniciar polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown 
