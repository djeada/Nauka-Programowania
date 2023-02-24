#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby n, poprosi
#uzytkownika o podanie n liczb i zwroci ich srednia aryt.

srednia() {

    n=$1
    suma=0

    for (( i=0; i<$n; i++ )); do
        read x
        suma=$(($suma + $x))
    done

    wynik=$(bc -l <<< "scale=2; $suma/$n")

    echo $wynik
}

main() {
    echo "Podaj liczbe n: "
    read n

    echo "Wprowadz $n liczb: "
    wynik=$(srednia $n)
    echo "srednia arytmetyczna z podanych liczb: $wynik"
}

main "$@"

