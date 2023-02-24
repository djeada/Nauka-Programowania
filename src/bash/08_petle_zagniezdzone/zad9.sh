#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby N,
#wypisze trojkat pascala o wysokosci N.


pascal() {

    for (( i=1; i<=$1; i++ ))
    do
        k=1
        for (( j=1; j<=$(($1-$i)); j++ ))
        do
            echo -n " "
        done

        for (( j=1; j<=$i; j++ ))
        do
            echo -n "$k "
            k=$(($k*($i - $j)/$j))
        done
        echo ""
    done
}


main() {

    pascal 5

}

main "$@"

