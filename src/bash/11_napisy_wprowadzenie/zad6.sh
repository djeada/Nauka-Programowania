#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Zamien litery a na znaki zapytania.

zamien() {
    sed -r 's/[a]+/?/g' <<< "$1"
}

test1() {
    local napis="pacZka!"
    local wynik="p?cZk?!"
    assertEqual "$(zamien "$napis")" "$wynik" $LINENO
}

main() {
    test1
}


main "$@"

