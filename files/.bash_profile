source ~/.git-prompt.sh
PS1='\[\e[0;32m\]$(__git_ps1 "(%s)")\[\e[m\]\[\e[0;31m\]\u@\w \d \t\n>\[\e[m\]'
export PS1
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

alias ls='ls --color=auto'
alias ll='ls -al'

if [ -f /usr/local/etc/bash_completion ]; then
    . /usr/local/etc/bash_completion
fi

### TheFuck
alias fuck='$(thefuck $(fc -ln -1))'
