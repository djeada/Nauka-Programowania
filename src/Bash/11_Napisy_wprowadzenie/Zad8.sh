#!/usr/bin/env bash

source ../assert.sh

#Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe.
#Wypisz pionowo slowa, z ktorych sklada sie zdanie.
#Znaki interpunkcyjne nie sa liczone jako slowa.

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # sparawdz czy napis jest alfanumeryczny
        # i zawiera co najmniej jedna litere
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo"
        fi
    done

}

main() {
    local zdanie="We think in generalities, but we live in details."
    wypisz_slowa "$zdanie"
}


main "$@"

