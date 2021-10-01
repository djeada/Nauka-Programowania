#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Zamien wszystkie
# male litery na wielkie.

na_wielkie_v1() {
    awk '{ print toupper($0) }' <<< "$1"
}

na_wielkie_v2() {
    tr a-z A-Z <<< "$1"
}

test1() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v1 "$napis")" "$wynik" $LINENO
}

test2() {
    local napis="pacZka!"
    local wynik="PACZKA!"
    assertEqual "$(na_wielkie_v2 "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

