#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie listy. Usun z pierwszej listy te
# elementy, ktore wystepuja rowniez w drugiej liscie.

usun_czesc_wspolna_v1() {
    for elem_a in "${lista_a[@]}"; do
        for elem_b in "${lista_b[@]}"; do
            if [ $elem_a -eq $elem_b ]; then
                lista_a=("${lista_a[@]/$elem_a}")
                break
            fi
        done
    done
}

usun_czesc_wspolna_v2() {

    lista_a=(
        $(echo ${lista_a[@]} ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -d | xargs echo ${lista_a[@]} | sed 's/ /\n/g' | sort | uniq -u)
    )
}

test1() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(7 9)
    usun_czesc_wspolna_v1
    assertSetsEqual lista_a oczekiwane $LINENO
}

test2() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(7 9)
    usun_czesc_wspolna_v2
    assertSetsEqual lista_a oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

