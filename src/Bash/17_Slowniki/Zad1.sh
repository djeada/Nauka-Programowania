#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie 
# z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi 
# od otrzymanej liczby oraz wartosci bedacych kwadratami 
# odpowiadajacych im kluczy.

zbuduj_slownik() {
    local liczba=$1
    local -A slownik=()
    for ((i=0; i<liczba; i++)); do
        slownik[$i]=$((i*i))
    done
    # iterujemy po kluczach i wartosciach
    # wypisujemy klucz i wartosc
    for k in "${!slownik[@]}"; do
        echo "$k: ${slownik[$k]};"
    done
}

test_zbuduj_slownik() {
    local wynik=($(zbuduj_slownik 10))
    local oczekiwane=("0: 0;" "1: 1;" "2: 4;" "3: 9;" "4: 16;" "5: 25;" "6: 36;" "7: 49;" "8: 64;" "9: 81;")
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_zbuduj_slownik
}


main "$@"

