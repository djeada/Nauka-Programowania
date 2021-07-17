#!/usr/bin/env bash

#Znajdz maksimum z czterech liczb.

main() {
    
    echo "Podaj cztery liczby."
    read a
    read b
    read c
    read d

    maxAB=$([ $a -gt $b ] && echo "$a" || echo "$b")
    maxCD=$([ $c -gt $d ] && echo "$c" || echo "$d")
    max=$([ $maxAB -gt $maxCD ] && echo "$maxAB" || echo "$maxCD")

    echo $max
}

main "$@"

