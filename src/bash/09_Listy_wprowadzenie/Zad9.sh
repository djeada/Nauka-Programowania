#!/usr/bin/env bash

source ../assert.sh

# Usun wszystkie wystapienia klucza z listy.
# Kolejnosc elementow w liscie powinna zostac zachowana.

usun_duplikaty() {
    local pom=()
    declare -A histo

    for liczba in "${lista[@]}"; do
        if [[ -z  ${histo["$liczba"]} ]]; then
            pom+=("$liczba")
            histo["$liczba"]=1
        fi
    done
    lista=("${pom[@]}")
    unset histo
    unset pom
}

test1() {
    local lista=(3 5 3 3 2)
    local wynik=(3 5 2)
    usun_duplikaty
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
}


main "$@"

