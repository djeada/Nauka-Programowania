#!/usr/bin/env bash

# Otrzymujesz napis oraz liczbe k.
# a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
# b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.

wypisz_poziomo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for((i=0;i<n;i+=k)); do
        echo -n "${napis:$i:1} "
    done
    echo ""
}

wypisz_pionowo() {
    local napis="$1"
    local k=$2
    local n=${#napis}

    for((i=0;i<n;i+=k)); do
        echo "${napis:$i:1} "
    done
}

main() {
    local napis="hej dzieci jesli chcecie zobaczyc smerfow las"
    local k=3

    wypisz_poziomo "$napis" $k
    wypisz_pionowo "$napis" $k
}


main "$@"

