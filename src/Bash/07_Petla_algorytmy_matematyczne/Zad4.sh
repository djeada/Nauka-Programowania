#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora przy pomocy petli obliczy silnie, 
#z otrzymanej liczby.

silnia() {
    
    a=$1
    wynik=1
    
    while [ $a -gt 0 ]; do 
        wynik=$(($wynik * $a))
        a=$(($a - 1))
    done

    echo $wynik
}

#Testy
test1() {
    a=0
    wynik=1
    assert "$wynik -eq $(silnia $a $b)" $LINENO
}

test2() {
    a=4
    wynik=24
    assert "$wynik -eq $(silnia $a $b)" $LINENO
}

main() {
    test1
    test2
}

main "$@"

