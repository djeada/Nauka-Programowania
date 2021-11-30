#!/usr/bin/env bash

source ../assert.sh

# Zaimplementuj sortowanie przez wstawianie.

sortuj(){
    local -n _tablica_ref=$1

    for (( i=1; i<${#_tablica_ref[@]}; i++ )); do
        local tmp=${_tablica_ref[$i]}
        local j=$((i-1))
        while (( j>=0 && _tablica_ref[j]>tmp )); do
            _tablica_ref[$((j+1))]=${_tablica_ref[$j]}
            ((j--))
        done
        _tablica_ref[$((j+1))]=$tmp
    done
}

test_sortuj() {
    local tablica=(4 2 5 3 1)
    local oczekiwane=(1 2 3 4 5)
    sortuj tablica
    assertArrayEqual tablica oczekiwane $LINENO
}

main() {
    test_sortuj
}


main "$@"

