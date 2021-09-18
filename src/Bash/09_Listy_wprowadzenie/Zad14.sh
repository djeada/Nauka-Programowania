#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy skladajacej sie z nieparzystej
# liczby elementow znajdz element bez pary. Przez pary
# elementow rozumiemy tutaj elementy o rownej wartosci.

element_bez_pary() {
    wynik=0

    for liczba in "${lista[@]}"; do
        wynik=$((wynik ^ liczba))
    done

    return $wynik
}

test1() {
    local lista=(1 3 1 7 3 1 1)
    local wynik=7
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 2 3 3 5 5 4)
    local wynik=4
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

