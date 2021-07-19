#!/usr/bin/env bash

#Dla pobranej od uzytkownika liczby, zwroc liczbe cyfr pobranje liczby.

main() {

    echo "Podaj liczbe: "
    read a

    licznik=0

    while [ $a -gt 0 ]
    do
        a=$(( $a / 10 ))
        licznik=$(($licznik + 1))
    done

    echo "Podana cyfra sklada sie z $licznik cyfr."

}

main "$@"

