#!/usr/bin/env bash

#Pros uzytkownika o podanie liczby, dopoki nie zostanie podana liczba 7.

main() {
    
    a=0

    while [ $a -ne 7 ]; do
        echo "Podaj liczbe:"
          read a
    done

}

main "$@"

