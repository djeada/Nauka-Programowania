#!/usr/bin/env bash

# Dla liczby N, wczytaj N liczb do listy, a nastepnie:
# a) dodaj do kazdego elementu 1;
# b) pomnoz kazdy element przez jego indeks;
# c) zastap wszystkie elementy wartoscia pierwszego elementu listy.
# Dla kazdego podpunktu wypisz zmodyfikowana liste. Elementy listy powinny
# byc oddzielone przecinkami i wypisane w jednym wierszu.

wczytaj() {

    for (( i=0; i<$1; i++ ))
    do
        read liczba
        lista+=("$liczba")
    done

}

zwieksz() {

    n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        lista[$i]=$((lista[$i] + 1))
    done
}

pomnoz() {

    n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        lista[$i]=$((lista[$i] * $i))
    done
}

zastap() {

    n=$(( ${#lista[@]}))

    for (( i=1; i<n; i++ ))
    do
        lista[$i]=${lista[0]}
    done
}

wypisz() {

    echo $(IFS=",";echo "${lista[*]// /|}";IFS=$'')

}

main() {

    declare -a lista
    echo "podaj liczbe n:"
    read n

    echo "podaj $n liczb:"
    wczytaj $n
    kopia=("${lista[@]}")

    echo -e "\nliczby powiekszone o 1:"
    zwieksz
    wypisz

    lista=("${kopia[@]}")

    echo -e "\nliczby pomnozone przez indeks:"
    pomnoz
    wypisz

    lista=("${kopia[@]}")

    echo -e "\npierwsza liczba $n razy:"
    zastap
    wypisz

}

main "$@"

