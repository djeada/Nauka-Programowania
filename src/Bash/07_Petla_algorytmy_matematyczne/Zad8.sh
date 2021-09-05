#!/usr/bin/env bash

source ../assert.sh

#Napisz funkcje, ktora dla otrzymanej liczby
#sprawdzi czy jest ona liczba pierwsza.

czyPierwsza() {

    a=$1

    if [[ $a -eq 2 ]] || [[ $a -eq 3 ]]; then
        echo true
        return
    fi

    if [[ $(($a % 2)) -eq 0 ]] || [[ $(($a % 3)) -eq 0 ]]; then
        echo false
        return
    fi

    i=3

    while [[ $((i * i)) -le $a ]]; do

        if [[ $(($a % i)) -eq 0 ]]; then
            echo false
            return
         fi

        i=$((i + 2))
    done

    echo true
    return
}


#Testy
test1() {
    a=7
    assertTrue "$(czyPierwsza $a)" $LINENO
}

test2() {
    a=4
    assertFalse "$(czyPierwsza $a)" $LINENO
}

test3() {
    a=1
    assertTrue "$(czyPierwsza $a)" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

