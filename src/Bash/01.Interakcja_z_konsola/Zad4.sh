#!/usr/bin/env bash

#Wypisz wynik podstawowych operacji arytmetycznych dla dwoch liczb pobranych od uzytkownika.

main() {
    
    echo "Podaj dwie liczby."
    read a
    read b

    echo "Suma pobranych liczb: $(($a + $b))"
    echo "Roznica pobranych liczb: $(($a - $b))"
    echo "Iloczyn pobranych liczb: $(($a * $b))"
    echo "Iloraz pierwszej przez druga: $(($a / $b))"
    echo "Reszta z dzielenia pierwszej przez druga: $(($a % $b))"
    echo "Pierwsza podniesiona do potegi rownej drugiej: $(($a ** $b))"

}

main "$@"

