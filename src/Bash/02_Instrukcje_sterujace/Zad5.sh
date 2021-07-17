#!/bin/bash

main() {
    #Dla trzech pobranych liczb, wypisz je w kolejnosci rosnacej.

    echo "Podaj trzy liczby:"
    read a
    read b
    read c

    if [[ $a -ls $b && $a -ls $c ]]; then
        if [[ $b -ls $c ]]; then
            echo $a
            echo $b
            echo $c
        else
             echo $a
            echo $c
            echo $b
        fi
    
    elif [[ $b -ls $a && $b -ls $c ]]; then
        if [[ $a -ls $c ]]; then
            echo $b
            echo $a
            echo $c
        else
             echo $b
            echo $c
            echo $a
        fi
    else
        if [[ $a -ls $b ]]; then
            echo $c
            echo $a
            echo $b
        else
             echo $c
            echo $b
            echo $a
        fi
    fi
}

main "$@"
