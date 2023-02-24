#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora dla otrzymanej liczby
#zwroci jej pierwiastek.

pierwiastek() {

    a=$1
    wynik="${a}.0"

    while [ 1 -eq $(echo "$wynik*$wynik - $a > 0.0001" | bc -l) ]; do
        wynik=$(echo "scale=5; ($wynik + $a/$wynik)/2" | bc -l)
    done

    echo ${wynik/.*}
}


#Testy
test1() {
    a=16
    wynik=4
    assert "$wynik -eq $(pierwiastek $a $b)" $LINENO
}

main() {
    test1
}

main "$@"

