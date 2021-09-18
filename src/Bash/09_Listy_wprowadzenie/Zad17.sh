#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy oraz liczby x, znajdz indeksy pierwszej
# pary elementow listy, ktorych suma jest rowna liczbie x.
# Jesli w liscie nie ma takiej pary, zwroc pare (-1, -1)

suma_dwoch() {
    local n=${#lista[@]}
    local liczba=$1

    for (( i=0; i<n; i++ )); do
        for (( j=i+1; j<n; j++ )); do
            if [ $((lista[i] + lista[j])) -eq $liczba ]; then
                echo "($i, $j)"
                return
            fi
        done
    done

    echo "(-1, -1)"
}

test1() {
    local lista=(1 3 4 5 2)
    local liczba=5
    local wynik="(0, 2)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

test2() {
    local lista=(2 -6 10 21 8)
    local liczba=7
    local wynik="(-1, -1)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

