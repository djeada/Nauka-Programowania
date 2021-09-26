#!/usr/bin/env bash

source ../assert.sh

#Dla otrzymanych dwoch list zwroc liste powstala poprzez:
#a) dostawienie drugiej listy na koniec pierwszej listy;
#b) wstawienie elementow o indeksach parzystych z drugiej listy
#na odpowiadajace im indeksy pierwszej listy.

dostaw() {
    wynik=("${lista_a[@]}" "${lista_b[@]}")
}

podmien() {
    local n=${#lista_a[@]}
    wynik=("${lista_a[@]}")

    for (( i = 0; i < n; i+=2)); do
        wynik[$i]=${lista_b[$i]}
    done
}

test1() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(-2 8 3 6 7 5 0)
    dostaw
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(7 8 0 6)
    podmien
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
}


main "$@"

