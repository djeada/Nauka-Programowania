#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb, kierunek przesuniec (1 odpowiada przesunieciu
# w prawo, a 0 w lewo) oraz liczbe miejsc o jaka maja zostac przesuniete
# elementy listy. Przykladowo dla przesuwania w prawo pierwszy element trafia
# na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego.
# Przesun elementy listy w danym kierunku.

rotacja() {
    local kierunek=$1
    local liczba=$2
    local n=$(($(( ${#lista[@]})) -1))

    if [[ $kierunek == "prawo" ]]; then
        for (( i = 0; i < liczba; i++)); do
            # prepend last element and remove from the back
            lista=(${lista[$n]}  "${lista[@]}")
            lista=( "${lista[@]:0:n+1}")
        done
    else
        for (( i = 0; i < liczba; i++)); do
            # append first element and remove from the front
            lista=( "${lista[@]}" ${lista[0]} )
            lista=( "${lista[@]:1}")
        done
    fi

}

test1() {
    local lista=(5 27 6 2 1 10 8)
    local wynik=(6 2 1 10 8 5 27)
    local kierunek="lewo"
    local liczba=2
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(9 9 42 47 5 6 19 7)
    local wynik=(6 19 7 9 9 42 47 5)
    local kierunek="prawo"
    local liczba=3
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

