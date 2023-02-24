#!/usr/bin/env bash

#Pobierz od uzytkownika trzy dlugosci bokow i sprawdz czy mozna z nich zbudowac trojkat.

main() {

    echo "Podaj trzy dlugosci bokow: "

    read a
    read b
    read c

    if [[ $(($a + $b)) > $c ]] && [[ $(($a + $c)) > $b ]] && [[ $(($b + $c)) > $a ]]; then
        echo "Z podanych dlugosci bokow mozna zbudowac trojkat"

    else
        echo "Z podanych dlugosci bokow nie mozna zbudowac trojkata"
    fi
}

main "$@"

