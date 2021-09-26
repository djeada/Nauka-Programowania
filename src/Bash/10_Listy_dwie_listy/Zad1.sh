#!/usr/bin/env bash

#Dla otrzymanych dwóch list wypisz na przemian elementy pierwszej i drugiej listy.
#Jesli listy nie sa rownej dlugosci, po wyczerpaniu elementow krotszej listy,
#wypisuj tylko elementy dluzszej listy.

wypisz() {

    local n=$(( ${#lista_a[@]} ))
    local m=$(( ${#lista_b[@]} ))
    local min_dlugosc=$((n<m ? n : m))

    for (( i=0; i<min_dlugosc; i++ ))
    do
        echo -n "${lista_a[$i]}, "
        echo -n "${lista_b[$i]}, "
    done

    for (( i=min_dlugosc; i<n; i++ ))
    do
        echo -n "${lista_a[$i]}, "
    done

    for (( i=min_dlugosc; i<m; i++ ))
    do
        echo -n "${lista_b[$i]}, "
    done

    echo
}

main() {

    lista_a=(5 3 7 2)
    lista_b=(1 -2 3)

    wypisz

}

main "$@"

