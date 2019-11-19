alias n='nmap -T insane -sV --script vulners'
alias tko='git checkout origin/master --' 
alias gbs='git push --set-upstream origin $(git branch --show-current)'
alias np='n -p0-10000'
alias ga='git add'
alias gs='git status'
alias gc='git commit'
alias gp='git pull'
alias gpp='git push'
alias gb='git branch'
alias gk='git checkout'
alias gbc='gb --current-branch'
alias gd='git diff'
alias s='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
alias ec2='ssh -i ~/.ssh/w1zard_aws.pem ubuntu@54.200.143.110' 
alias gro='git rebase origin/master'
alias setup='ln -sf /dev/null ~/.zsh_history'
alias fmt='go fmt ./...'
alias check='go test -v ./... -cover -tags=integration | grep FAIL'
#requies ssh setup first
alias setup_scripts='mkdir scripts && cd scripts && git clone git@github.com:taylornelson/scripts-tools.git'

NAME='taylornelson'

alias rsa='ssh-keygen -t rsa ~/id_rsa && cat ~/.ssh/id_rsa.pub'
fmt_squash_check () {
	if [ $# -ne 1 ]
	then
		echo "supply no commits to squash"
	fi
	fmt && squash $1 && check
}

test () {
	echo $1
}
squash () {
	git reset --hard HEAD~$1 && git merge --squash HEAD@{1} && git commit
}

repo_init () {
	touch README.md
	git init
	git add README.md
	git commit -m "first commit"
	git remote add origin git@github.com:$NAME/$1.git
	git push -u origin master
}

HISTFILE="$HOME/.zsh_history"
HISTSIZE=10000000
SAVEHIST=10000000
setopt BANG_HIST                 # Treat the '!' character specially during expansion.
setopt EXTENDED_HISTORY          # Write the history file in the ":start:elapsed;command" format.
setopt INC_APPEND_HISTORY        # Write to the history file immediately, not when the shell exits.
setopt SHARE_HISTORY             # Share history between all sessions.
setopt HIST_EXPIRE_DUPS_FIRST    # Expire duplicate entries first when trimming history.
setopt HIST_IGNORE_DUPS          # Don't record an entry that was just recorded again.
setopt HIST_IGNORE_ALL_DUPS      # Delete old recorded entry if new entry is a duplicate.
setopt HIST_FIND_NO_DUPS         # Do not display a line previously found.
setopt HIST_IGNORE_SPACE         # Don't record an entry starting with a space.
setopt HIST_SAVE_NO_DUPS         # Don't write duplicate entries in the history file.
setopt HIST_REDUCE_BLANKS        # Remove superfluous blanks before recording entry.
setopt HIST_VERIFY               # Don't execute immediately upon history expansion.
