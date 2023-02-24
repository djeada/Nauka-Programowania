#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy, skladajacej sie z nieuporzadkowanych
# kolejnych (za wyjatkiem jednego) wyrazow ciagu arytmetycznego,
# znajdz brakujacy element.

znajdz_maks() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -nr | head -n1
}

znajdz_min() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -n | head -n1
}

suma_ciagu_art() {
    local n=${#lista[@]}
    min=$(znajdz_min)
    maks=$(znajdz_maks)
    echo $(bc -l <<< "scale=0; ($n+1)*($min+$maks)/2")
}

znajdz_brakujacy_element() {

    suma_listy=$(IFS=+; echo "$((${lista[*]}))")
    suma_przedzialu=$(suma_ciagu_art)

    return $((suma_przedzialu - suma_listy))
}

test1() {
    local lista=(6 8 4 10 14 2)
    local wynik=12
    znajdz_brakujacy_element
    assertEqual $? $wynik $LINENO
}

test2() {
    local lista=(1 2 4 5 6)
    local wynik=3
    znajdz_brakujacy_element
    assertEqual $? $wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

