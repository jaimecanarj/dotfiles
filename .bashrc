#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## synth-shell-prompt.sh
if [ -f /home/jaime/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
  source /home/jaime/.config/synth-shell/synth-shell-prompt.sh
fi