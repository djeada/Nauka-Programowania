#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby N
#wypisze N pierwszych wierszy i kolumn
#tabliczki mnozenia.

tabliczkaMnozenia() {

    a=$1

    for (( i=1; i<=$a; i++ )); do
        for (( j=1; j<=$a; j++ )); do
            echo -n "$(($i * $j)) "
        done
        echo ""
    done

}

main() {

    tabliczkaMnozenia 5

}

main "$@"

