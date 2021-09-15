#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste oraz klucz. Znajdz indeks odpowiadajacy pierwszemu
# wystapieniu klucza w liscie. Jesli klucz nie wysteþuje w liscie, zwroc -1.

znajdz_klucz_v1() {

    n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        if [ ${lista[$i]} -eq $1 ]; then
            echo $i
            return
        fi
    done

    echo -1
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    local a=2
    local wynik=6
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}

test2() {
    local lista=(3 -2 4 9 -3 -40 8 5 -7 -1)
    local a=2
    local wynik=-1
    assertEqual $(znajdz_klucz_v1 $a) $wynik $LINENO
}


main() {
    test1
    test2
}

main "$@"

