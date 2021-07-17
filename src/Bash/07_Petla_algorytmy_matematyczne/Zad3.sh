#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora dla otrzymanych dwoch liczb, 
#przy pomocy dodawania badz odejmowania oraz petli zrealizuje:

#a) mnozenie;
mnozenie() {
    
    a=$1
    b=$2
    wynik=0
    
    for (( i=0; i<$b; i++ )); do 
        wynik=$(($wynik + $a))
    done

    echo $wynik
}

#b) dzielenie
dzielenie() {
    a=$1
    b=$2
    wynik=0
    
    while [ $a -ge $b ]; do 
        a=$(($a - $b))
        wynik=$(($wynik + 1))
    done

    echo $wynik
}

#Testy
test1() {
    a=2
    b=3
    wynik=6
    assert "$wynik -eq $(mnozenie $a $b)" $LINENO
}

test2() {
    a=30
    b=6
    wynik=5
    assert "$wynik -eq $(dzielenie $a $b)" $LINENO

}

main() {
    test1
    test2
}

main "$@"

