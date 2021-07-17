#!/usr/bin/env bash

#Napisz funkcje, ktora dla otrzymanej liczby
#wyswietli N trojkatow. Trojkaty powinny byc 
#ustawione w kolumnie, jeden na drugim. Wysokosc 
#pierwszego trojkata to 1, a dla kazdego nastepnego 
#rowna jest wysokosci poprzedniego powiekszonej o 1.

trojkat() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<=$i; j++ )); do
            echo -n "x"
        done
        echo ""
    done

}

choinka() {

    n=$1

    for (( i=1; i<=$n; i++ )); do
        trojkat $i
    done

}

main() {

    choinka 5    

}

main "$@"

