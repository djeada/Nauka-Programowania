#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste par napisow i liczb. Posortuj pary w liscie wzgledem:
# a) Liczb.
# b) Dlugosci napisow.

posortuj_wzgledem_napisow() {
    local _lista_ref=("$@")
    echo "${_lista_ref[@]}" | tr ' ' '\n' | sort -u
}

posortuj_wzgledem_liczb() {
    local _lista_ref=("$@")
    echo "${_lista_ref[@]}" | tr ' ' '\n' | sort -t ':' -k 2 -n
}

test_posortuj_wzgledem_napisow() {
    local lista_par=('a:2' 'c:1' 'b:3')
    local wynik=($(posortuj_wzgledem_napisow "${lista_par[@]}"))
    local oczekiwane=('a:2' 'b:3' 'c:1')
    assertElementsEqual wynik oczekiwane $LINENO
}

test_posortuj_wzgledem_liczb() {
    local lista_par=('a:2' 'c:1' 'b:3')
    local wynik=($(posortuj_wzgledem_liczb "${lista_par[@]}"))
    local oczekiwane=('c:1' 'a:2' 'b:3')
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_posortuj_wzgledem_napisow
    test_posortuj_wzgledem_liczb
}

main "$@"

