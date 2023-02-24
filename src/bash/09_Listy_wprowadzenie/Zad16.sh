#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy liczb naturalnych, znajdz elemnt
# dominujacy. Element dominujacy to element, ktorego liczba
# wystapien w liscie jest wieksza niz polowa dlugosci listy.
# Jesli lista nie ma elementu dominujacego, zwroc -1.

znajdz_pary() {

    local n=${#lista[@]}
    local suma=$1

    for (( i=0; i<n; i++ )); do
        for (( j=i+1; j<n; j++ )); do
            if [ $((lista[i] + lista[j])) -eq $suma ]; then
                wynik+=("${lista[$i]}, ${lista[$j]};")
            fi
        done
    done
}

test1() {
    local lista=(0 4 5 6 2 9 2 3)
    local suma=5
    local oczekiwane=('0, 5;' '2, 3;' '2, 3;')
    declare -a wynik;
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

test2() {
    local lista=(1 -1 3 -3 4 5)
    local suma=0
    local oczekiwane=('1, -1;' '3, -3;')
    declare -a wynik;
    znajdz_pary $suma
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

