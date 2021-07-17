#!/usr/bin/env bash

#Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora 
#dla otrzymanych dwoch liczb zwroci: 

#a) ich sume

suma() {
    return $(($1 + $2))
}

#b) roznice drugiej i pierwszej

roznica() {
    return $(($2 - $1))
}

#c) ich iloczyn

iloczyn() {
    return $(($1 * $2))
}

#d) reszte z dzielenia pierwszej przez druga

reszta() {
    return $(($2 % $1))
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    suma $a $b
    wynik=$?
    echo "suma liczb to $wynik"

    roznica $a $b
      wynik=$?
    echo "iloczyn liczb to $wynik"

    iloczyn $a $b
      wynik=$?
    echo "suma liczb to $wynik"

    reszta $a $b
      wynik=$?
    echo "reszte z dzielenia pierwszej przez druga to $wynik"
}

main "$@"

