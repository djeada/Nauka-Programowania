#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liczbe n. Zwroc napis skladajacy
# sie z liczb naturalnych od 1 do n.

liczby() {

    local n="$1"
    local wynik=""

    for((i=1;i<=n;i++)); do
        local wynik="$wynik$i"
    done

    echo "$wynik"

}

test1() {
    local n=5
    local wynik="12345"
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

test2() {
    local n="-1"
    local wynik=""
    assertEqual "$(liczby $n)" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

