#!/usr/bin/env bash

source ../assert.sh

# Usun wszystkie wystapienia klucza z listy.
# Kolejnosc elementow w liscie powinna zostac zachowana.

usun() {
    local klucz=$1
    local pom=()
    for liczba in "${lista[@]}"
    do
        [ $liczba -ne $klucz ] && pom+=($liczba)
    done
    lista=("${pom[@]}")
    unset pom
}

test1() {
    local lista=(6 7 2 1 8)
    local wynik=(6 7 1 8)
    local klucz=2
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(1 1 1 1)
    local wynik=()
    local klucz=1
    usun $klucz
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
}


main "$@"

