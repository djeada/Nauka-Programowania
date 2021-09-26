#!/usr/bin/env bash

source ../assert.sh

#Otrzymujesz dwie listy liczb reprezentujacych wspolrzedne dwoch wektorow. Zaimplementuj:
#a) mnozenie skla<rne.
#b) mnozenie wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni euklidesowej).

mnozenie_skalarne() {

    local n=$(( ${#lista_a[@]} ))
    local wynik=0

    for (( i=0; i<n; i++ ))
    do
        wynik=$(echo "${lista_a[$i]} * ${lista_b[$i]}+$wynik" | bc -l)

    done
    echo "$wynik"
}

mnozenie_wektorowe() {

    wynik=()
    wynik+=($(echo "${lista_a[1]} * ${lista_b[2]} - ${lista_a[2]} * ${lista_b[1]}" | bc -l))
    wynik+=($(echo "${lista_a[2]} * ${lista_b[0]} - ${lista_a[0]} * ${lista_b[2]}" | bc -l))
    wynik+=($(echo "${lista_a[0]} * ${lista_b[1]} - ${lista_a[1]} * ${lista_b[0]}" | bc -l))
}


test1() {
    local lista_a=(3 -5 4)
    local lista_b=(2 6 5)
    local wynik=-4
    assertEqual "$(mnozenie_skalarne)" "$wynik" $LINENO
}

test2() {
    local lista_a=(3 -5 4)
    local lista_b=(2 6 5)
    local oczekiwane=(-49 -7 28)
    mnozenie_wektorowe
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
}


main "$@"

