#!/usr/bin/env bash

#Dla pobranej od uzytkownika liczby, zwroc wszystkie liczby:

main() {

    echo "Podaj liczbe: "
    read a

    #a) mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10

    echo "mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: "
    for (( i=0; i<$a; i++ )); do
        pom=$i
        suma=0

        while [ $pom -gt 0 ]; do
            suma=$(($suma + $pom % 10))
            pom=$(( $pom / 10 ))
        done

        if [[ $suma -eq 10 ]]; then
            echo $i
        fi
    done

    #b) dwucyfrowe mniejsze od pobranej liczby

    echo "dwucyfrowe mniejsze od pobranej liczby: "
    for (( i=10; i<100 && i <$a; i++ )); do
        echo $i
    done


    #c) trzycyfrowe ktorych suma cyfr jest    rowna pobranej liczbie
    echo "trzycyfrowe ktorych suma cyfr jest rowna pobranej liczbie"
    for (( i=100; i<1000; i++ )); do
        pom=$i
        suma=0

        while [ $pom -gt 0 ]; do
            suma=$(($suma + $pom % 10))
            pom=$(( $pom / 10 ))
        done

        if [[ $suma -eq $a ]]; then
            echo $i
        fi
    done

    #d) trzycyfrowe podzielne przez sume cyfr pobranej liczby
    echo "trzycyfrowe podzielne przez sume cyfr pobranej liczby"

    pom=$a
    suma=0

    while [ $pom -gt 0 ]; do
        suma=$(($suma + $pom % 10))
        pom=$(( $pom / 10 ))
    done

    for (( i=100; i<1000; i++ )); do

        if [[ $(($i % $suma)) -eq 0 ]]; then
            echo $i
        fi
    done

    #d) mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr
    echo "mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr"

    for (( i=0; i<$a; i++ )); do

        pom=$i
        flaga=true
        while [ $pom -gt 0 ]; do
            cyfra=$(($pom % 10))
            if [[ $(($cyfra % 2)) -ne 0 ]]; then
                flaga=false
                break
            fi
            pom=$(( $pom / 10 ))
        done

        if [[ "$flaga" == "true" ]]; then
            echo $i
        fi

    done


}

main "$@"

