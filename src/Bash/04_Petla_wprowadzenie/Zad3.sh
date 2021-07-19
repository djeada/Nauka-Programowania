#!/usr/bin/env bash

#Dla pobranej liczby, wyswietl liczbe Pi z dokladnoscia do tylu miejsc po przecinku ile wynosi pobrana liczba.

main() {

    echo "Podaj liczbe:"
    read a

    echo "scale=$a; 4*a(1)" | bc -l
}

main "$@"

