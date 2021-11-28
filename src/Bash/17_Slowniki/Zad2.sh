#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie listy liczb calkowitych. Zbuduj slownik skladajacy sie z 
# kluczy bedacych elementami pierwszej listy i wartosciami bedacymi elementami 
# drugiej listy. Jesli listy sa roznej dlugosci zwroc pusty slownik.

zbuduj_slownik() {
    local -a lista_a=($1)
    local -a lista_b=($2)
    local -A slownik=()
    local n=${#lista_a[@]}

    for ((i=0; i<n; i++)); do
        slownik[${lista_a[i]}]=${lista_b[i]}
    done

    for k in "${!slownik[@]}"; do
        echo "$k: ${slownik[$k]};"
    done
}

test_zbuduj_slownik() {
    local wynik=($(zbuduj_slownik "1 2 3 4 5" "a b c d e"))
    local oczekiwane=(
        "1: a;"
        "2: b;"
        "3: c;"
        "4: d;"
        "5: e;"
    )
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_zbuduj_slownik
}


main "$@"

