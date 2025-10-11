#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

## synth-shell-prompt.sh
if [ -f ~/.config/synth-shell/synth-shell-prompt.sh ] && [ -n "$( echo $- | grep i )" ]; then
  source ~/.config/synth-shell/synth-shell-prompt.sh
fi

## Alias
alias ls="eza --icons"
alias cat="bat"