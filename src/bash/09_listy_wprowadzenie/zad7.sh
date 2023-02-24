#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy znajdz liczbe mniejsza
# od najwiekszej liczby z listy i jednoczesnie
# wieksza od wszystkich pozostalych.

wieksza() {
    local n=${#lista[@]}

    if [ $n -eq 0 ]; then
        echo "0.00"
        return
    fi

    if [ $n -eq 1 ]; then
        echo $((lista[0]- 1))
        return
    fi

    local maks="$((1<<63))"
    local maks2="$((1<<63))"

    for liczba in "${lista[@]}" ; do

        if [ $liczba -gt $maks ]; then
            maks2=$maks;
            maks=$liczba;
        elif  [ $liczba -gt $maks ]; then
            maks2=$liczba
        fi
    done

    echo $(bc -l <<< "scale=2; ($maks+$maks2)/2")
}

main() {
    local lista=(3 5 -7 4 9 -11 2)
    echo $(wieksza)
}

main "$@"

