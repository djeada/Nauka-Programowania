#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie posortowane listy rownej
# dlugosci. Znajdz ich mediane.

mediana() {
    local n=${#lista_a[@]}
    local m=${#lista_b[@]}

    local i=0
    local j=0
    local m1=-1
    local m2=-1

    for (( licznik = 0; licznik <= (n+m)/2; licznik++)); do

        if [ $(((m + n) % 2)) -eq 0 ]; then
            m2=$m1;
        fi

        if [ $i -ne $n ] && [ $j -ne  $m ]; then
            if [ ${lista_a[$i]} -gt ${lista_b[$j]} ]; then
                m1=${lista_b[$j]}
                j=$((j+1))
            else
                m1=${lista_a[$i]}
                i=$((i+1))
            fi
        elif [ $i -lt $n ]; then
            m1=${lista_a[$i]}
            i=$((i+1))
        else
            m1=${lista_b[$j]}
            j=$((j+1))
        fi
    done

    if [ $(((m + n) % 2)) -eq 1 ]; then
        echo $m1
    else
        echo $(bc -l <<< "scale=2; ($m1+$m2)/2")
    fi

}

test1() {
    local lista_a=(2 4 7)
    local lista_b=(3 5 9)
    local wynik=4.50
    assertEqual $(mediana) $wynik $LINENO
}

main() {
    test1
}

main "$@"

