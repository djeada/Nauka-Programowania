#!/bin/bash

main() {
    #Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

    echo "Podaj liczbe:"
    read x

    if [[ $x -gt 0 ]]; then
        echo "Liczba jest dodatnia."
    elif [[ $x -lt 0 ]]; then
        echo "Liczba jest ujemna."
    else
        echo "Liczba jest zerem."
    fi
}

main "$@"
