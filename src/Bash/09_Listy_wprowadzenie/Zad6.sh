#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb. Sprwadz czy srednia elementow
# znajduje sie w liscie. Dla sredniej nie bedacej liczba
# calkowita, zaokraglij wynik w dol.

srednia() {
    local suma=$(IFS=+; echo "$((${lista[*]}))")
    local n=${#lista[@]}
    echo $((suma/n))
}

czy_srednia_w_liscie() {

    local srednia_wartosc=$(srednia)
    for elem in "${lista[@]}"; do
        if [ $elem -eq $srednia_wartosc ]; then
            echo true
            return
        fi
    done

    echo false
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    assertFalse "$(czy_srednia_w_liscie)" $LINENO
}

test2() {
    local lista=(1 2 3)
    assertTrue "$(czy_srednia_w_liscie)" $LINENO
}


main() {
    test1
    test2
}

main "$@"

