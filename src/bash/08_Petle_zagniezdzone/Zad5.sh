#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby N
#wypisze N pierwszych wierszy i kolumn
#tabliczki mnozenia.

literaX() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<$a; j++ )); do
            if [ $i -eq $j ] || [ $j -eq $(($a - $i - 1)) ]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done

}

main() {

    literaX 5

}

main "$@"

