#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste skladajaca sie wylacznie z liter A i B.
# Litera A reprezentuje samochod jadacy na wschod, a
# litera B jadacy na zachod.  Samochody jadace w przeciwna
# strony mijaja sie. Policz mijajace sie samochody.

policz_samochody() {
    local licznik=0
    local pom=0

    for litera in "${lista[@]}"; do
        if [[ $litera == 'A' ]]; then
            pom=$((pom+1))
        elif [[ $litera == 'B' ]]; then
            licznik=$((licznik+pom))
        fi
    done

    return $licznik
}

test1() {
    local lista=('A' 'B' 'A' 'B' 'B')
    local wynik=5
    policz_samochody
    assertEqual $? $wynik $LINENO
}

test2() {
    local lista=('A' 'A' 'A' 'B' 'B' 'A' 'B' 'A' 'B' 'A' 'A' 'A')
    local wynik=15
    policz_samochody
    assertEqual $? $wynik $LINENO
}


main() {
    test1
    test2
}

main "$@"

