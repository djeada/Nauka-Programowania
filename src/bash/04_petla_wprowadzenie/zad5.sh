#!/usr/bin/env bash

# Dla pobranych dwoch liczb, powinny zostac wypisane:
# a) Wszystkie liczby naturalne wieksze od mniejszej pobranej liczby 
# i jednoczesnie mniejsze od wiekszej pobranej liczby. 
# b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej 
# pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.

main() {

    echo "Podaj dwie liczby:"
    read a
    read b

    if [[ $a -gt $b ]]; then
        echo "swap"
        temp=$a
        a=$b
        b=$temp
    fi

    echo "Liczby naturalne wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        echo $i
    done

    echo "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        if [[ $(($i % 3)) -eq 0 ]]; then
            echo $i
        fi
    done
}

main "$@"

