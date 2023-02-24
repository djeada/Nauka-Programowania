#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza 
# liczbe calkowita. Usun ze slownika pary, dla ktorych wartosc rowna 
# jest otrzymanej liczbie.

usun_ze_slownika() {
    local klucz="$1"

    for k in "${!slownik[@]}"; do
        if [[ ${slownik["$k"]} == "$klucz" ]]; then
            unset slownik["$k"]
        fi
    done
}

test_usun_ze_slownika() {
    local -A slownik=( [a]=1 [b]=2 [c]=3 [d]=1 )
    local -A oczekiwane_wartosci=([b]=2 [c]=3)
    usun_ze_slownika 1
    assertArrayEqual slownik oczekiwane_wartosci
}

main() {
    test_usun_ze_slownika
}


main "$@"

