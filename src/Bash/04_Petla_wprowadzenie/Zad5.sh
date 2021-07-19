#!/usr/bin/env bash


main() {


    echo "Podaj dwie liczby:"
    read a
    read b

    #Dla pobranych dwoch liczb, powinny zostac wyswietlone wszystkie liczby naturalne wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby.

    if [[ $a -gt $b ]]; then
        echo "swap"
        temp=$a
        a=$b
        b=$temp
    fi

    echo "liczby naturalne wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        echo $i
    done

    #Dla pobranych dwoch liczb, powinny zostac wyswietlone wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby.

    echo "liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i mniejsze od wiekszej pobranej liczby: "

    for (( i=$(($a+1)); i<$b; i++ )); do
        if [[ $(($i % 3)) -eq 0 ]]; then
            echo $i
        fi
    done
}

main "$@"

