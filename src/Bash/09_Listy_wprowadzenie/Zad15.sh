#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy liczb naturalnych, znajdz elemnt
# dominujacy. Element dominujacy to element, ktorego liczba
# wystapien w liscie jest wieksza niz polowa dlugosci listy.
# Jesli lista nie ma elementu dominujacego, zwroc -1.

element_dominujacy() {
    declare -A histo

    local n=${#lista[@]}

    for liczba in "${lista[@]}"; do
        if [[ -z  ${histo["$liczba"]} ]]; then
            histo["$liczba"]=1
        else
            histo["$liczba"]=$((${histo["$liczba"]} + 1))
        fi

    done

    for klucz in "${!histo[@]}"
    do
        if [ ${histo[$klucz]} -gt $((n/2)) ]; then
            unset histo
            echo "$klucz"
            return
        fi
    done

    unset histo
    echo "-1"
}

test1() {
    local lista=(4 7 4 4 2)
    local wynik=4
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

test2() {
    local lista=(1 2 4 5 6)
    local wynik=-1
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

