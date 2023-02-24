#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb.
# Zamien liste na napis.

liczby() {
    printf -v wynik '%s' "${lista[@]}"
    echo "$wynik"
}

test1() {
    local lista=(1 2 3 4)
    local wynik="1234"
    assertEqual "$(liczby)" "$wynik" $LINENO
}

test2() {
    local lista=()
    local wynik=""
    assertEqual "$(liczby)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

