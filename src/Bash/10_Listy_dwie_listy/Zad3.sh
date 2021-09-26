#!/usr/bin/env bash

source ../assert.sh

#Dla otrzymanych dwoch list, zwroc liste, ktorej elementy sa suma odpowiadajacych
#sobie elementow otrzymanych list.  Jesli listy nie sa rownej dlugosci, zaloz ze
#brakujace elementy krotszej listy sa rowne 0.

suma() {

    local n=$(( ${#lista_a[@]} ))
    local m=$(( ${#lista_b[@]} ))
    local min_dlugosc=$((n<m ? n : m))
    wynik=("${lista_a[@]}")

    for (( i=0; i<min_dlugosc; i++ ))
    do
        wynik[$i]=$((wynik[i] + lista_b[i]))
    done

    for (( i=min_dlugosc; i<m; i++ ))
    do
        wynik+=("{lista_b[$i]}")
    done

}

test1() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 8 10)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8)
    local oczekiwane=(5 9 2 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test3() {
    local lista_a=(3 1 0 0)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 6 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
    test3
}


main "$@"

