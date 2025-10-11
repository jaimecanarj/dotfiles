#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

export QT_QPA_PLATFORMTHEME=qt5ct
export PHPSTORM_JDK="/usr/lib/jvm/default"

# PHP y Laravel
export PATH="~/.config/herd-lite/bin:$PATH"
export PHP_INI_SCAN_DIR="~/.config/herd-lite/bin:$PHP_INI_SCAN_DIR"