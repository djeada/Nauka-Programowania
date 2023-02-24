#!/usr/bin/env bash

#Napisz funkcje, ktora:

#a) dla podanych dwoch liczb, zwroci mniejsza

min2() {

    if [[ $1 -lt $2 ]] ; then
        return $1
    else
        return $2
    fi
}

#b) dla podanych dwoch liczb, zwroci wieksza

maks2() {

    if [[ $1 -gt $2 ]] ; then
        return $1
    else
        return $2
    fi
}


#c) dla podanych trzech liczb, zwroci najmniejsza

min3() {
    if [[ $1 -le $2 && $1 -le $3 ]]; then
        return $1
    elif [[ $2 -le $1 && $2 -le $3 ]]; then
        return $2
    else
        return $3
    fi
}

#d) dla podanych trzech liczb, zwroci najwieksza

maks3() {
    if [[ $1 -ge $2 && $1 -ge $3 ]]; then
        return $1
    elif [[ $2 -ge $1 && $2 -ge $3 ]]; then
        return $2
    else
        return $3
    fi
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    min2 $a $b
    wynik=$?
    echo "mniejsza liczba to $wynik"

    maks2 $a $b
    wynik=$?
    echo "wieksza liczba to $wynik"

    echo "Podaj trzy liczby: "
    read a
    read b
    read c

    min3 $a $b $c
    wynik=$?
    echo "najmniejsza liczba to $wynik"

    maks3 $a $b $c
    wynik=$?
    echo "najwieksza liczba to $wynik"

}

main "$@"

