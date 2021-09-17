#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb, wykonaj nastepujace polecenia:
# a)Zwieksz o 1 wszystkie elementy stojace na parzystych indeksach.
# b)Wyzeruj wszystkie wielokrotnosci liczby 3.
# c)Podnies do kwadratu wszystkie elementy mniejsze niz 10.
# d)Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami
# pierwszymi.
# e)Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.

zwieksz() {
    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        if [ $((i % 2)) -eq 0 ]; then
            lista[$i]=$((lista[$i] + 1))
        fi
    done

}

wyzeruj() {
    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        if [ $((lista[$i] % 3)) -eq 0 ]; then
            lista[$i]=0
        fi
    done

}

kwadrat(){
    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        elem=${lista[$i]}
        if [ $elem -lt 10 ]; then
            lista[$i]=$((elem*elem))
        fi
    done

}

czy_pierwsza() {

    local a=$1

    if [[ $a -lt 2 ]]; then
        echo false
        return
    fi

    if [[ $a -eq 2 ]] || [[ $a -eq 3 ]]; then
        echo true
        return
    fi

    if [[ $(($a % 2)) -eq 0 ]] || [[ $(($a % 3)) -eq 0 ]]; then
        echo false
        return
    fi

    i=3

    while [[ $((i * i)) -le $a ]]; do

        if [[ $(($a % i)) -eq 0 ]]; then
            echo false
            return
        fi

        i=$((i + 2))
    done

    echo true
    return
}

suma(){
    local suma_elementow=$(IFS=+; echo "$((${lista[*]}))")
    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        if [[ $(czy_pierwsza $i) == "true" ]]; then
            lista[$i]=$suma_elementow
        fi
    done
}

zamien() {
    declare -a iloczyny
    local n=$(( ${#lista[@]}))

    for (( i=0; i<n; i++ ))
    do
        local iloczyn=1
        for (( j=0; j<n; j++ ))
        do

            if [ $i -ne $j ]; then
                iloczyn=$((iloczyn * lista[$j]))
            fi
        done
        iloczyny+=("$iloczyn")
    done

    lista=(${iloczyny[*]})
}


test1() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=(4 5 -6 4 10 -11 3)
    zwieksz
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=(0 5 -7 4 0 -11 2)
    wyzeruj
    assertArrayEqual lista wynik $LINENO
}

test3() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=(9 25 49 16 81 121 4)
    kwadrat
    assertArrayEqual lista wynik $LINENO
}

test4() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=(3 5 5 5 9 5 2)
    suma
    assertArrayEqual lista wynik $LINENO
}

test5() {
    local lista=(3 5 -7 4 9 -11 2)
    local wynik=(27720 16632 -11880 20790 9240 -7560 41580)
    zamien
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
    test3
    test4
    test5
}

main "$@"

