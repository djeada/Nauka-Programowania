#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwie listy: wagi oraz wartosci.
# Znajdz srednia wazona wartosci.

srednia_wazona() {
    local n=${#wartosci[@]}
    local suma=0
    local suma_iloczynow=0

    for (( i=0; i<n; i++ ))
    do
        suma=$(echo "${wartosci[$i]} + $suma" | bc -l)
        suma_iloczynow=$(echo "${wartosci[$i]} * ${wagi[$i]} + $suma_iloczynow" | bc -l)
    done

    echo $(bc -l <<< "scale=2; $suma_iloczynow/$suma")
}

test1() {
    local wartosci=(0 -23 -5 2 -3 4 9)
    local wagi=(1 2 3 4 5 6 7)
    local wynik=-1.18
    assertEqual "$(srednia_wazona)" "$wynik" $LINENO
}

test2() {
    local wartosci=(2 5 0 2 1)
    local wagi=(0.2 0.4 0.1 0.2 0.1)
    local wynik=.29
    assertEqual "$(srednia_wazona)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

