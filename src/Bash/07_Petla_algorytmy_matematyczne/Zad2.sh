#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora dla otrzymanych dwoch liczb
#przy pomocy petli obliczy ile wynosi a podniesione do b.

potega() {

    a=$1
    b=$2
    wynik=1

    for (( i=0; i<$b; i++ )); do
        wynik=$(($wynik * $a))
    done

    echo $wynik
}

main() {
    a=2
    b=3
    wynik=8
    assert "$wynik -eq $(potega $a $b)" $LINENO
}

main "$@"

