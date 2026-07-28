_lsusers_completion() {
    local cur="${COMP_WORDS[COMP_CWORD]}"
    COMPREPLY=( $(compgen -W "all human system count --json --csv --names --help --version" -- "$cur") )
}
complete -F _lsusers_completion lsusers
