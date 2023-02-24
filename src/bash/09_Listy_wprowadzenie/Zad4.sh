#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste. Znajdz najwiekszy
# i najmniejszy element tej listy.

maks_v1() {
    local maks=${lista[0]}
    for elem in "${lista[@]}" ; do
        ((elem > maks)) && maks=$elem
    done
    echo $maks
}

min_v1() {
    local min=${lista[0]}
    for elem in "${lista[@]}" ; do
        ((elem < min)) && min=$elem
    done
    echo $min
}

maks_v2() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -nr | head -n1
}

min_v2() {
    IFS=$'\n'
    echo "${lista[*]}" | sort -n | head -n1
}


test1() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=9
    assertEqual $(maks_v1) $wynik $LINENO
}

test2() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=-11
    assertEqual $(min_v1) $wynik $LINENO
}

test3() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=9
    assertEqual $(maks_v2) $wynik $LINENO
}

test4() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=-11
    assertEqual $(min_v2) $wynik $LINENO
}


main() {
    test1
    test2
    test3
    test4
}

main "$@"

