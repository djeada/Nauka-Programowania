#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste oraz klucz. Znajdz indeks odpowiadajacy pierwszemu
# wystapieniu klucza w liscie. Jesli klucz nie wysteþuje w liscie, zwroc -1.

srednia() {
    suma=$(IFS=+; echo "$((${lista[*]}))")
    n=$(( ${#lista[@]}))
    echo $((suma/n))
}

czy_srednia_w_liscie() {

    srednia_wartosc=$(srednia)
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

