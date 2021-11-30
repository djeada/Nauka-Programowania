#!/usr/bin/env bash

# Zaimplementuj sortowanie szybkie.

partycja() {
    local i=$1
    local j=$2
    j=$((j-2))
    local klucz=${_tablica_ref[j+1]}

    while [ $i -le $j ]; do
        if [ ${_tablica_ref[i]} -le $klucz ]; then
            i=$((i+1))
        elif [ ${_tablica_ref[j]} -ge $klucz ]; then
            j=$((j-1))
        else
            local tmp=${_tablica_ref[i]}
            _tablica_ref[i]=${_tablica_ref[j]}
            _tablica_ref[j]=$tmp
            i=$((i+1))
            j=$((j-1))
        fi
    done
    j=$2
    j=$((j-1))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[j]}
    _tablica_ref[j]=$tmp

    return $i
}  

_sortuj() {
    local start=$1
    local stop=$2

    if [ $((stop-start)) -lt 2 ]; then
        return
    fi

    local i=$((start+RANDOM%(stop-start)))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[stop-1]}
    _tablica_ref[stop-1]=$tmp
    partycja $start $stop
    i=$?

    _sortuj $start $i
    _sortuj $((i+1)) $stop
}

sortuj() {
    local -n _tablica_ref=$1
    _sortuj 0 ${#_tablica_ref[@]}
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
