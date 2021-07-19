#!/usr/bin/env bash

main() {

    echo "Podaj liczbe:"
    read n

    #Dla pobranej liczby n wyswietl n pierwszych wyrazow ciagu danego wzorem n/(n+1)

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(echo "scale=2; $i/$(($i + 1))" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n/(n+1) dla n=$n: $suma"

    #Dla pobranej liczby n wyswietl n pierwszych wyrazow ciagu danego wzorem (n^2 + 5)/n

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(echo "scale=2; $(($n**2 + 5))/$n" | bc)
        suma=$(echo "scale=2; $suma + $a_n" | bc)

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem (n^2 + 5)/n dla n=$n: $suma"

    #Dla pobranej liczby n wyswietl n pierwszych wyrazow ciagu danego wzorem n + 2^n

    suma=0

    for (( i=1; i<=$n; i++ )); do
        a_n=$(($n + 2**$n))
        suma=$(($suma + $a_n))

    done

    echo "suma n pierwszych wyrazow ciagu danego wzorem n + 2^n dla n=$n: $suma"

}

main "$@"

