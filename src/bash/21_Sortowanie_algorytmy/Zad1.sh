#!/usr/bin/env bash

source ../assert.sh

# Zaimplementuj sortowanie babelkowe.

sortuj(){
    local -n _tablica_ref=$1

    for (( i=0; i<${#_tablica_ref[@]}-1; i++ )); do
        for (( j=i+1; j<${#_tablica_ref[@]}; j++ )); do
            if [[ ${_tablica_ref[i]} -gt ${_tablica_ref[j]} ]]; then
                local tmp=${_tablica_ref[i]}
                _tablica_ref[i]=${_tablica_ref[j]}
                _tablica_ref[j]=$tmp
            fi
        done
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

