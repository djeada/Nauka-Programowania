#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby
#wypisze kwadrat o boku rownym otrzymanej liczbie.


kwadrat() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<$a; j++ )); do
            echo -n "x"
        done
        echo ""
    done

}

main() {

    kwadrat 5


}

main "$@"

