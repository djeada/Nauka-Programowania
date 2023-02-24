#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie posortowane listy.
# Polacz je w posortowana liste.

polacz_v1() {
    wynik=()

    local n=${#lista_a[@]}
    local m=${#lista_b[@]}

    if [ $n -eq 0 ] || [ $m -eq 0 ]; then
        return
    fi

    local i=0
    local j=0

    while [ $i -lt $n ] && [ $j -lt $m ]
    do
        if [ ${lista_a[$i]} -lt ${lista_b[$j]} ]; then
            wynik+=("${lista_a[$i]}")
            i=$((i+1))
        else
            wynik+=("${lista_b[$j]}")
            j=$((j+1))
        fi
    done

    while [ $i -lt $n ]
    do
        wynik+=("${lista_a[$i]}")
        i=$((i+1))
    done

    while [ $j -lt $m ]
    do
        wynik+=("${lista_b[$j]}")
        j=$((j+1))
    done

}

test1() {
    local lista_a=(5 7 11)
    local lista_b=(1 3 8 14)
    local oczekiwane=(1 3 5 7 8 11 14)
    polacz_v1
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
}


main "$@"

