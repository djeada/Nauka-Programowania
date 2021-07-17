#!/usr/bin/env bash

#Dla pobranej liczby powinny zostac wyswietlone wszystkie liczby naturalne mniejsze od pobranej liczby.

main() {
    
    echo "Podaj liczbe:"
      read a

    while [ $a -gt 0 ]; do
        a=$(($a-1))
        echo $a
    done

}

main "$@"

