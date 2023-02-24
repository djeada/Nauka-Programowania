#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie listy. Znajdz elementy wystepujace
# zarowno w pierwszej jak i w drugiej liscie.

czesc_wspolna_v1() {
    wynik=()
    for elem_a in "${lista_a[@]}"; do
        for elem_b in "${lista_b[@]}"; do
            if [ $elem_a -eq $elem_b ]; then
                wynik+=( "$elem_a" )
                break
            fi
        done
    done
}

czesc_wspolna_v2() {
    wynik=($(echo -n $(echo ${lista_a[@]} ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -d)))
}

test1() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(3 6 2)
    czesc_wspolna_v1
    assertSetsEqual wynik oczekiwane $LINENO
}

test2() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(3 6 2)
    czesc_wspolna_v2
    assertSetsEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}


main "$@"

