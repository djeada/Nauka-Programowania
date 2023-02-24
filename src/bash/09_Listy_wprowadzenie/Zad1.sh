#!/usr/bin/env bash

#Dla liczby N, wczytaj N liczb do listy, a nastepnie:
# a) wypisz liste od poczatku do konca. Elementy listy powinny
# znajdowac sie w osobnych wierszach.
# b) wypisz liste od konca. Elementy listy powinny byc oddzielone
# przecinkami i wypisane w jednym wierszu.

wczytaj() {

    for (( i=0; i<$1; i++ ))
    do
        read liczba
        lista+=("$liczba")
    done

}

wypisz_od_poczatku() {

    for liczba in "${lista[@]}"
    do
        echo "$liczba"
    done
}

wypisz_od_konca() {

    local n=$(( ${#lista[@]} -1 ))

    for (( i=n; i>=0; i-- ))
    do
        echo "${lista[$i]}"
    done
}

main() {

    declare -a lista
    echo "podaj liczbe n:"
    read n

    echo "podaj $n liczb:"
    wczytaj $n

    echo -e "\nliczby w kolejnosci wczytania:"
    wypisz_od_poczatku

    echo -e "\nliczby wypisane od konca:"
    wypisz_od_konca

}

main "$@"

