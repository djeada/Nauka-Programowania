#!/usr/bin/env bash

#Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora
#dla otrzymanych dwoch liczb ustali czy:

#a) pierwsza liczba jest wieksza od drugiej

czyWieksza() {

    if [[ $1 -gt $2 ]] ; then
        echo true
    else
        echo false
    fi
}

#b) czy suma liczb jest mneijsza niz 10

czySumaMniejsza() {
    suma=$(($1 + $2))

    if [[ $suma -lt 10 ]] ; then
        echo true
    else
        echo false
    fi
}

#c) czy obie sa nieparzyste

czyObieNieparzyste() {
    if [[ $(($1 % 2)) -eq 1 ]] && [[ $(($2 % 2)) -eq 1 ]]; then
        echo true
    else
        echo false
    fi
}

#d) czy wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu

wieksza() {
    if [[ $1 > $2 ]]; then
        return $1
    else
        return $2
    fi
}

czyWiekszaNizKwad() {
    wieksza $1 $2
    wieksza=$?

    if [[ $wieksza -lt $(($1**2)) ]]; then
        echo true
    else
        echo false
    fi
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    wynik=$(czyWieksza $a $b)
    echo "Pierwsza liczba jest wieksza od drugiej: $wynik"

    wynik=$(czySumaMniejsza $a $b)
    echo "Suma liczb jest mniejsza od 10: $wynik"

    wynik=$(czyObieNieparzyste $a $b)
    echo "Obie liczby nieparzyste: $wynik"

    wynik=$(czyWiekszaNizKwad $a $b)
    echo "Wieksza liczba jest mniejsza od pierwszej podniesionej do kwadratu $wynik"
}

main "$@"

