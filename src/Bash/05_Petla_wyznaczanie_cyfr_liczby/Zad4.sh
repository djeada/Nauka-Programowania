#!/usr/bin/env bash

#Dla pobranej liczby, powinny zostac zwrocone cyfry liczby spelniajce nastepujacy warunek:

main() {

    echo "Podaj liczbe: "
    read a

    #a) Liczby parzyste;

    pom=$a
    echo "Cyfry liczby badace liczbami parzystymi: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $(($cyfra % 2)) -eq 0 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

    #b) Mniejsze niz 5;

    pom=$a
    echo "Cyfry liczby mniejsze niz 5: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $cyfra -lt 5 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

    #c) Rozne od 0;

    pom=$a
    echo "Cyfry liczby rozne od 0: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $cyfra -ne 0 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

}

main "$@"

